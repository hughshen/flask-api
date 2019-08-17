from flask import Flask, request, render_template
from settings import AppConfig
from middlewares import auth
from routes import Router
from models import db
from handlers.site import site_bp
from helpers.helper import res_json

app = Flask(__name__)
app.config.from_object(AppConfig)
app.register_blueprint(site_bp)

Router.init(app)

db.init_app(app)

@app.before_request
def before_request_auth():
    resp = auth.api_token_middleware(request)
    if resp is not None:
        return resp

@app.errorhandler(404)
def not_found_handler(error):
    if request.path.startswith('/api/'):
        return res_json(code='000002'), 404
    else:
        return render_template('404.html'), 404

@app.errorhandler(Exception)
def system_error_handler(error):
    app.logger.error(error)
    return res_json(code='000001'), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0')
