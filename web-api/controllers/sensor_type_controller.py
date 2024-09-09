from flask import Blueprint, jsonify, request
from ..extensions import db
from ..repositories.sensor_type_repository import SensorTypeRepository
from ..services.sensor_type_service import SensorTypeService
from ..models.sensor_type_model import SensorTypeModel

sensor_type_blueprint = Blueprint('sensor_type', __name__)

sensor_type_repository = SensorTypeRepository(db.session)
sensor_type_service = SensorTypeService(sensor_type_repository)

@sensor_type_blueprint.route('/sensor-types', methods=['GET'])
def get_sensor_types():
    data = sensor_type_service.get_all()
    return jsonify([{'id': d.id, 'type': d.type} for d in data]), 200

@sensor_type_blueprint.route('/sensor-types', methods=['POST'])
def create_sensor_type():
    type_data = request.json
    new_data = SensorTypeModel(
        type=type_data.get("type")
    )
    created_data = sensor_type_service.create(new_data)
    if created_data:
        return jsonify({'id': created_data.id, 'type': created_data.type}), 201
    else:
        return jsonify({"message": "Failed to create sensor type"}), 400

@sensor_type_blueprint.route('/sensor-types/<int:type_id>', methods=['GET'])
def get_sensor_type_by_id(type_id):
    data = sensor_type_service.get_by_id(type_id)
    if data:
        return jsonify({'id': data.id, 'type': data.type}), 200
    else:
        return jsonify({"message": "Sensor type not found"}), 404

@sensor_type_blueprint.route('/sensor-types/<int:type_id>', methods=['PUT'])
def update_sensor_type(type_id):
    type_data = request.json
    data = sensor_type_service.get_by_id(type_id)
    if data:
        data.type = type_data.get("type")
        updated_data = sensor_type_service.update(data)
        return jsonify({'id': updated_data.id, 'type': updated_data.type}), 200
    else:
        return jsonify({"message": "Sensor type not found"}), 404

@sensor_type_blueprint.route('/sensor-types/<int:type_id>', methods=['DELETE'])
def delete_sensor_type(type_id):
    deleted_data = sensor_type_service.delete(type_id)
    if deleted_data:
        return jsonify({"message": f"Sensor type {type_id} deleted"}), 204
    else:
        return jsonify({"message": "Sensor type not found"}), 404
