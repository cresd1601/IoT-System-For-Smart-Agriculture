import os
from flask import Flask, request, jsonify
from alembic import command
from alembic.config import Config

from .extensions import db

# Import the controllers with correct names
from .controllers.location_controller import location_blueprint
from .controllers.sensor_controller import sensor_blueprint
from .controllers.temperature_data_controller import temperature_data_blueprint
from .controllers.humidity_data_controller import humidity_data_blueprint
from .controllers.moisture_data_controller import moisture_data_blueprint
from .controllers.sensor_type_controller import sensor_type_blueprint
from .controllers.setting_controller import setting_blueprint

app = Flask(__name__)


# Manually add CORS headers
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    return response


app.after_request(add_cors_headers)

# Database configuration
app.config[
    'SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@{os.getenv('CLOUD_SERVICE_IP')}/{os.getenv('MYSQL_DATABASE')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with the app
db.init_app(app)

# Register the blueprints with the /api prefix
app.register_blueprint(location_blueprint, url_prefix='/api')
app.register_blueprint(sensor_blueprint, url_prefix='/api')

app.register_blueprint(temperature_data_blueprint, url_prefix='/api')
app.register_blueprint(humidity_data_blueprint, url_prefix='/api')
app.register_blueprint(moisture_data_blueprint, url_prefix='/api')

app.register_blueprint(sensor_type_blueprint, url_prefix='/api')
app.register_blueprint(setting_blueprint, url_prefix='/api')

def apply_migrations():
    alembic_cfg = Config(os.path.join(os.path.dirname(__file__), 'alembic.ini'))
    command.upgrade(alembic_cfg, 'head')

@app.before_first_request
def before_first_request_func():
    apply_migrations()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
