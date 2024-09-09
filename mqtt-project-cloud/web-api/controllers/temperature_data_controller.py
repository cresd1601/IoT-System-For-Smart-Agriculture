from flask import Blueprint, jsonify, request
from ..extensions import db
from ..repositories.sensor_temperature_data_repository import SensorTemperatureDataRepository
from ..repositories.sensor_repository import SensorRepository
from ..repositories.location_repository import LocationRepository
from ..repositories.setting_repository import SettingRepository
from ..services.temperature_data_service import TemperatureDataService

temperature_data_blueprint = Blueprint('temperature_data', __name__)

# Initialize repositories
sensor_temperature_data_repository = SensorTemperatureDataRepository(db.session)
sensor_repository = SensorRepository(db.session)
location_repository = LocationRepository(db.session)
setting_repository = SettingRepository(db.session)

# Initialize service with repositories
temperature_data_service = TemperatureDataService(
    temperature_data_repository=sensor_temperature_data_repository,
    sensor_repository=sensor_repository,
    location_repository=location_repository,
    setting_repository=setting_repository
)

@temperature_data_blueprint.route('/temperature-data', methods=['GET'])
def get_temperature_data():
    """Fetch all temperature data for a given sensor_id"""
    sensor_id = request.args.get('sensor-id', type=int)

    if sensor_id is None:
        return jsonify({"error": "sensor_id is required"}), 400

    try:
        data = temperature_data_service.get_all_by_sensor_id(sensor_id)
        return jsonify(data), 200
    except Exception as e:
        print(f"Error fetching temperature data for sensor {sensor_id}: {e}")
        return jsonify({"error": "An error occurred while fetching the temperature data."}), 500


@temperature_data_blueprint.route('/temperature-data/chart', methods=['GET'])
def get_temperature_chart_data():
    """Fetch the latest temperature chart data for a given sensor_id, including min and max temperatures."""
    sensor_id = request.args.get('sensor-id', type=int)

    if sensor_id is None:
        return jsonify({"error": "sensor_id is required"}), 400

    try:
        # Fetch chart data including min and max temperature levels
        chart_data = temperature_data_service.get_chart_data_by_sensor_id(sensor_id)
        return jsonify(chart_data), 200
    except Exception as e:
        print(f"Error fetching temperature chart data for sensor {sensor_id}: {e}")
        return jsonify({"error": "An error occurred while fetching the temperature chart data."}), 500
