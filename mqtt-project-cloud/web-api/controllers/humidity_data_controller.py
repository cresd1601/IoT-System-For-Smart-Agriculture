from flask import Blueprint, jsonify, request
from ..extensions import db
from ..repositories.sensor_temperature_data_repository import SensorTemperatureDataRepository
from ..repositories.sensor_repository import SensorRepository
from ..repositories.location_repository import LocationRepository
from ..repositories.setting_repository import SettingRepository
from ..services.humidity_data_service import HumidityDataService

humidity_data_blueprint = Blueprint('humidity_data', __name__)

# Initialize repositories
sensor_temperature_data_repository = SensorTemperatureDataRepository(db.session)
sensor_repository = SensorRepository(db.session)
location_repository = LocationRepository(db.session)
setting_repository = SettingRepository(db.session)

# Initialize service with repositories
humidity_data_service = HumidityDataService(sensor_temperature_data_repository, sensor_repository, location_repository, setting_repository)

@humidity_data_blueprint.route('/humidity-data', methods=['GET'])
def get_humidity_data():
    """API endpoint to get detailed humidity data for a specific sensor."""
    # Get sensor_id from query parameters
    sensor_id = request.args.get('sensor-id', type=int)

    if sensor_id is None:
        return jsonify({"error": "sensor_id is required"}), 400

    # Fetch data for the specific sensor_id
    data = humidity_data_service.get_all_by_sensor_id(sensor_id)

    # Return JSON response
    return jsonify(data), 200

@humidity_data_blueprint.route('/humidity-data/chart', methods=['GET'])
def get_humidity_chart_data():
    """API endpoint to get chart data for humidity levels for the past 10 minutes, including min/max values."""
    # Get sensor_id from query parameters
    sensor_id = request.args.get('sensor-id', type=int)

    if sensor_id is None:
        return jsonify({"error": "sensor_id is required"}), 400

    # Fetch chart data for the specific sensor_id
    chart_data = humidity_data_service.get_chart_data_by_sensor_id(sensor_id)

    # Return JSON response
    return jsonify(chart_data), 200
