from flask import Blueprint, jsonify, request
from ..extensions import db
from ..repositories.sensor_repository import SensorRepository
from ..services.sensor_service import SensorService
from ..models.sensor_model import SensorModel

sensor_blueprint = Blueprint('sensor', __name__)

sensor_repository = SensorRepository(db.session)
sensor_service = SensorService(sensor_repository)

@sensor_blueprint.route('/sensors', methods=['GET'])
def get_sensors():
    data = sensor_service.get_all()
    return jsonify([
        {
            'id': d.id,
            'name': d.name,
            'type_id': d.type_id,
            'location_id': d.location_id,
            'type': d.type.type if d.type else None,
            'location': d.location.name if d.location else None
        } for d in data
    ]), 200

@sensor_blueprint.route('/sensors', methods=['POST'])
def create_sensor():
    sensor_data = request.json
    new_sensor = SensorModel(
        name=sensor_data.get("name"),
        type_id=sensor_data.get("type_id"),
        location_id=sensor_data.get("location_id")
    )
    created_sensor = sensor_service.create(new_sensor)
    if created_sensor:
        return jsonify({
            'id': created_sensor.id,
            'name': created_sensor.name,
            'type_id': created_sensor.type_id,
            'location_id': created_sensor.location_id,
            'type': created_sensor.type.type if created_sensor.type else None,
            'location': created_sensor.location.name if created_sensor.location else None
        }), 201
    else:
        return jsonify({"message": "Failed to create sensor"}), 400

@sensor_blueprint.route('/sensors/<int:sensor_id>', methods=['GET'])
def get_sensor_by_id(sensor_id):
    sensor = sensor_service.get_by_id(sensor_id)
    if sensor:
        return jsonify({
            'id': sensor.id,
            'name': sensor.name,
            'type_id': sensor.type_id,
            'location_id': sensor.location_id,
            'type': sensor.type.type if sensor.type else None,
            'location': sensor.location.name if sensor.location else None
        }), 200
    else:
        return jsonify({"message": "Sensor not found"}), 404

@sensor_blueprint.route('/sensors/<int:sensor_id>', methods=['PUT'])
def update_sensor(sensor_id):
    sensor_data = request.json
    sensor = sensor_service.get_by_id(sensor_id)
    if sensor:
        sensor.name = sensor_data.get("name")
        sensor.type_id = sensor_data.get("type_id")
        sensor.location_id = sensor_data.get("location_id")
        updated_sensor = sensor_service.update(sensor)
        return jsonify({
            'id': updated_sensor.id,
            'name': updated_sensor.name,
            'type_id': updated_sensor.type_id,
            'location_id': updated_sensor.location_id,
            'type': updated_sensor.type.type if updated_sensor.type else None,
            'location': updated_sensor.location.name if updated_sensor.location else None
        }), 200
    else:
        return jsonify({"message": "Sensor not found"}), 404

@sensor_blueprint.route('/sensors/<int:sensor_id>', methods=['DELETE'])
def delete_sensor(sensor_id):
    deleted_sensor = sensor_service.delete(sensor_id)
    if deleted_sensor:
        return jsonify({"message": f"Sensor {sensor_id} deleted"}), 204
    else:
        return jsonify({"message": "Sensor not found"}), 404
