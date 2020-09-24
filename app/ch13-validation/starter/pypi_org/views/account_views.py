import flask

from pypi_org.infrastructure import request_dict
from pypi_org.infrastructure.view_modifiers import response
from pypi_org.services import user_service
import pypi_org.infrastructure.cookie_auth as cookie_auth
from pypi_org.viewmodels.account.index_viewmodel import IndexViewModel
from pypi_org.viewmodels.account.register_viewmodel import RegisterViewModel

blueprint = flask.Blueprint('account', __name__, template_folder='templates')


# ################### INDEX #################################


@blueprint.route('/account')
@response(template_file='account/index.html')
def index():
    vm = IndexViewModel()

    if not vm.user:
        return flask.redirect('/account/login')

    return vm.to_dict()


# ################### REGISTER #################################

@blueprint.route('/account/register', methods=['GET'])
@response(template_file='account/register.html')
def register_get():
    vm = RegisterViewModel()
    return vm.to_dict()


@blueprint.route('/account/register', methods=['POST'])
@response(template_file='account/register.html')
def register_post():
    vm = RegisterViewModel()

    vm.validate()

    if vm.error:
        return vm.to_dict()

    user = user_service.create_user(vm.name, vm.email, vm.password)
    if not user:
        return vm.to_dict()

    resp = flask.redirect('/account')
    cookie_auth.set_auth(resp, user.id)

    return resp


# ################### LOGIN #################################

@blueprint.route('/account/login', methods=['GET'])
@response(template_file='account/login.html')
def login_get():
    return {}


@blueprint.route('/account/login', methods=['POST'])
@response(template_file='account/login.html')
def login_post():
    data = request_dict.create(default_val='')

    email = data.email.lower().strip()
    password = data.password.strip()

    if not email or not password:
        return {
            'email': email,
            'password': password,
            'error': "Some required fields are missing.",
            'user_id': cookie_auth.get_user_id_via_auth_cookie(flask.request),
        }

    user = user_service.login_user(email, password)
    if not user:
        return {
            'email': email,
            'password': password,
            'error': "The account does not exist or the password is wrong.",
            'user_id': cookie_auth.get_user_id_via_auth_cookie(flask.request),
        }

    resp = flask.redirect('/account')
    cookie_auth.set_auth(resp, user.id)

    return resp


# ################### LOGOUT #################################

@blueprint.route('/account/logout')
def logout():
    resp = flask.redirect('/')
    cookie_auth.logout(resp)

    return resp
