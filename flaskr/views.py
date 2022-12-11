import os
from flask import Blueprint, request, jsonify, render_template, Response
import numpy as np
from .models import BankData, User
from datetime import datetime
import xgboost as xgb
import shap
import pandas as pd

view = Blueprint('view', __name__)

MODEL_PATH = os.path.join(os.getcwd(), "data/full_model_09122022_2.bin")
MODEL = xgb.XGBClassifier()
MODEL.load_model(MODEL_PATH)


@view.route('/')
@view.route('/index')
@view.route('/home')
def view_home():
    return render_template('index.html')


@view.route('/customer-list')
def view_customer_list():
    all_users = User.query.all()
    response = list(map(lambda u: u.as_dict(), all_users))
    print("Get all users", response)
    return render_template('customer_list.html', users=all_users)


@view.route('/customer-information')
def view_customer_information():
    id = request.args.get('ID')
    new = request.args.get('new', 'False')
    new = True if new == 'True' else False
    user = User.query.filter_by(ID=id).first()
    # print(f'New: {isinstance(new,bool)}')
    # print(user.as_dict())
    # user = User()
    if new:
        return render_template('customer_information.html', user=user, new=new)
    print(user.as_dict())
    return render_template('customer_information.html', user=user, new=new)


@view.route('/admin-score')
def view_admin_score():
    id = request.args.get('ID')
    user = User.query.filter_by(ID=id).first()
    user_info = BankData.query.filter_by(ID=id).first()
    data = user_info.as_dict()
    user = user.as_dict()
    print(user)
    data["CODE_GENDER"] = user["gender"]
    data["DAYS_BIRTH"] = (datetime.today(
    ) - datetime.strptime(user["birthday"], '%Y-%m-%d')).days
    data["DAYS_EMPLOYED"] = (
        datetime.today() - datetime.strptime(user["day_employed"], '%Y-%m-%d')).days
    data["DAYS_ID_PUBLISH"] = (
        datetime.today() - datetime.strptime(user["day_ID_publish"], '%Y-%m-%d')).days
    keys = list(data.keys())[1:]
    input_values = np.asarray([[data[i] for i in keys]])
    result = MODEL.predict_proba(input_values)
    pos = result[0][0]
    neg = result[0][1]
    print({"probability_1": pos, "probability_0": neg})
    score = int(pos*550 + 300)
    rating = ""
    value = pd.read_csv(os.path.join(
        os.getcwd(), "data/train_df.csv"), index_col=False)
    value.drop(columns=value.columns[0],
               axis=1,
               inplace=True)
    explainer_shap = shap.Explainer(MODEL)
    shap_values = explainer_shap(value)
    force_plot = shap.plots.force(shap_values[0], contribution_threshold=0.5)
    print(value.columns)
    shap_html = f"<head>{shap.getjs()}</head><body>{force_plot.html()}</body>"
    if score >= 800:
        rating = "Great"
    elif score >= 740:
        rating = "Very Good"
    elif score >= 670:
        rating = "Good"
    elif score >= 580:
        rating = "Fair"
    else:
        rating = "Poor"
    fico = {"score": score, "percentage": int(
        pos*100), "ID": id, "rating": rating}
    return render_template('admin_score.html', fico=fico, shap_plots=shap_html)


@view.route('/check')
def helping():
    id = request.args.get('ID')
    return render_template('Check.html', id=id)
