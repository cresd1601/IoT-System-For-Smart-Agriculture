from flask import Blueprint, jsonify, request
from ..extensions import db
from ..repositories.sensor_temperature_data_repository import SensorTemperatureDataRepository
from ..repositories.sensor_repository import SensorRepository
from ..repositories.location_repository import LocationRepository
from ..services.humidity_data_service import HumidityDataService

humidity_data_blueprint = Blueprint('humidity_data', __name__)

# Initialize repositories
sensor_temperature_data_repository = SensorTemperatureDataRepository(db.session)
sensor_repository = SensorRepository(db.session)
location_repository = LocationRepository(db.session)

# Initialize service with repositories
humidity_data_service = HumidityDataService(sensor_temperature_data_repository, sensor_repository, location_repository)

@humidity_data_blueprint.route('/humidity-data', methods=['GET'])
def get_humidity_data():
    # Get sensor_id from query parameters
    sensor_id = request.args.get('sensor-id', type=int)

    if sensor_id is None:
        return jsonify({"error": "sensor_id is required"}), 400

    # Fetch data for the specific sensor_id
    data = humidity_data_service.get_all_by_sensor_id(sensor_id)

    # Return JSON response
    return jsonify(data), 200
