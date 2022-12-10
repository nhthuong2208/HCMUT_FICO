from flask import Blueprint, request, jsonify
from .models import *
from .utils import *
import numpy as np
import xgboost as xgb

main = Blueprint('main', __name__)

MODEL_PATH = os.path.join(os.getcwd(), "data/full_model_09122022_2.bin")
MODEL = xgb.XGBClassifier()
MODEL.load_model(MODEL_PATH)

@main.route('/')
def main_page():
    return 'Welcome to PICO'

# ADD new user
@main.route('/user', methods=['POST'])
def add_user():
    request_data = request.get_json()

    new_user = User(request_data)

    db.session.add(new_user)
    db.session.commit()

    return {"success":new_user.ID}

# GET the user with SS number
@main.route('/user/<string:ssNum>', methods=['GET', 'POST'])
def get_user(ssNum):
    try:
        user = User.query.filter_by(SS_number=ssNum).first()
        if request.method == "POST":
            data = request.get_json()
            user.ID = data["ID"]
            user.SS_number = data["SS_number"]
            user.birthday = data["birthday"]
            user.address = data["address"]
            user.first_name = data["first_name"]
            user.last_name = data["last_name"]
            user.phone = data["phone"]
            user.gender = data["gender"]
            user.email = data["email"]
            user.day_ID_publish = data["day_ID_publish"]
            user.day_employed = data["day_employed"]

            db.session.add(user)
            db.session.commit()

            return jsonify({"success":True})
        elif request.method == "GET":
            return jsonify({"result":user.as_dict()})
    except BaseException as err:
        return jsonify(err=str(err)), 500

# GET all users
@main.route('/user/all')
def get_all_users():
    try:
        all_users = User.query.all()
        response = list(map(lambda u: u.as_dict(), all_users))
        return jsonify(response)
    except BaseException as err:
        return jsonify(err=str(err)), 500

@main.route('/history')
def get_history():
    pass

@main.route('/model/score', methods=["POST"])
def get_score():
    pass
    request_data = request.get_json()
    user_info = BankData.query.filter_by(ID=request_data["id"]).first()
    data = user_info.as_dict()
    data["CODE_GENDER"] = request_data["gender"]
    data["DAYS_BIRTH"] = request_data["birthday"]
    data["DAYS_EMPLOYED"] = request_data["dayEmployed"]
    data["DAYS_ID_PUBLISH"] = request_data["dayIDPublish"]
    keys = list(data.keys())[1:]
    input_values = np.asarray([[data[i] for i in keys]])
    result = MODEL.predict_proba(input_values)
    pos = str(result[0][0])
    neg = str(result[0][1])
    return jsonify({"probability_0":pos,"probability_1":neg})

@main.route('/model/explainable')
def get_explain_for_model():
    pass



"""
    These APIs is used to add data to database and testing
    Don't call these APIs
"""

@main.route('/data/add', methods=['POST'])
def add_data():
    data_set = read_dataset()
    data = []
    for index in range(len(data_set) - 90):
        row = {}
        for col in COL_NAMES:
            row[col] = data_set.loc[index][col]
            data.append(row)

    for row in data:
        new_line = BankData(row)
        db.session.add(new_line)
        db.session.commit()

    return jsonify({"success":True})

@main.route('data/get')
def get_all():
    data = BankData.query.all()
    response = list(map(lambda x: x.as_dict(), data))

    return jsonify(response)