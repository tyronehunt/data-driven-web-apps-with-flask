import flask
from infrastructure.view_modifiers import response

app = flask.Flask(__name__)

def get_latest_packages():
    return [
        {'name': 'flask', 'version': '1.2.3', 'id': '1'},
        {'name': 'sqlalchemy', 'version': '2.2.3', 'id':2},
        {'name': 'passlib', 'version': '3.0.0', 'id':3, 'summary':'pending'},
    ]

@app.route('/')
@response(template_file='home/index.html')
def index():
    test_packages = get_latest_packages()
    return {'packages': test_packages}

@app.route('/about')
@response(template_file='home/about.html')
def about():
    return {}

if __name__ == '__main__':
    app.run(debug=True)