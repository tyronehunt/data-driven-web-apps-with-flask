import flask

from starter.pypi_org.infrastructure.view_modifiers import response
import starter.pypi_org.services.package_service as package_service

blueprint = flask.Blueprint('home', __name__, template_folder='templates')

@blueprint.route('/')
@response(template_file='home/index.html')
def index():
    test_packages = package_service.get_latest_packages()
    return {'packages': test_packages}


@blueprint.route('/about')
@response(template_file='home/about.html')
def about():
    return {}