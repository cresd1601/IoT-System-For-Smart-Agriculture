from flask import Blueprint, jsonify, request
from ..extensions import db
from ..repositories.sensor_moisture_data_repository import SensorMoistureDataRepository
from ..repositories.sensor_repository import SensorRepository
from ..repositories.location_repository import LocationRepository
from ..services.moisture_data_service import MoistureDataService

moisture_data_blueprint = Blueprint('moisture_data', __name__)

# Initialize repositories
sensor_moisture_data_repository = SensorMoistureDataRepository(db.session)
sensor_repository = SensorRepository(db.session)
location_repository = LocationRepository(db.session)

# Initialize service with repositories
moisture_data_service = MoistureDataService(sensor_moisture_data_repository, sensor_repository, location_repository)

@moisture_data_blueprint.route('/moisture-data', methods=['GET'])
def get_moisture_data():
    # Get sensor_id from query parameters
    sensor_id = request.args.get('sensor-id', type=int)

    if sensor_id is None:
        return jsonify({"error": "sensor_id is required"}), 400

    # Fetch data for the specific sensor_id
    data = moisture_data_service.get_all_by_sensor_id(sensor_id)

    # Return JSON response
    return jsonify(data), 200
