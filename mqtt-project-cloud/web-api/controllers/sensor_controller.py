from flask import Blueprint, jsonify, request
from ..extensions import db
from ..repositories.sensor_repository import SensorRepository
from ..services.sensor_service import SensorService

sensor_blueprint = Blueprint('sensor', __name__)

# Initialize repository and service
sensor_repository = SensorRepository(db.session)
sensor_service = SensorService(sensor_repository)

# Get all sensors
@sensor_blueprint.route('/sensors', methods=['GET'])
def get_sensors():
    data = sensor_service.get_all()
    return jsonify(data), 200

# Create a new sensor
@sensor_blueprint.route('/sensors', methods=['POST'])
def create_sensor():
    sensor_data = request.json
    created_sensor = sensor_service.create(sensor_data)
    if created_sensor:
        return jsonify(created_sensor), 201
    else:
        return jsonify({"message": "Failed to create sensor"}), 400

# Get sensor by ID
@sensor_blueprint.route('/sensors/<int:sensor_id>', methods=['GET'])
def get_sensor_by_id(sensor_id):
    sensor = sensor_service.get_by_id(sensor_id)
    if sensor:
        return jsonify(sensor), 200
    else:
        return jsonify({"message": "Sensor not found"}), 404

# Update sensor by ID
@sensor_blueprint.route('/sensors/<int:sensor_id>', methods=['PUT'])
def update_sensor(sensor_id):
    sensor_data = request.json
    updated_sensor = sensor_service.update(sensor_id, sensor_data)
    if updated_sensor:
        return jsonify(updated_sensor), 200
    else:
        return jsonify({"message": "Sensor not found"}), 404

# Delete sensor by ID
@sensor_blueprint.route('/sensors/<int:sensor_id>', methods=['DELETE'])
def delete_sensor(sensor_id):
    deleted_sensor = sensor_service.delete(sensor_id)
    if deleted_sensor:
        return jsonify({"message": f"Sensor {sensor_id} deleted"}), 204
    else:
        return jsonify({"message": "Sensor not found"}), 404
