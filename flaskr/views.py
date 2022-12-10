from flask import Blueprint, request, jsonify, render_template

from .models import User
view = Blueprint('view', __name__)


@view.route('/')
def view_main():
    return "Welcome to FICO view"


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
    return render_template('admin_score.html')
