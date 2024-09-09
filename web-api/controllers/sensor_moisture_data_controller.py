from flask import Blueprint, jsonify, request
from ..extensions import db
from ..repositories.sensor_moisture_data_repository import SensorMoistureDataRepository
from ..services.sensor_moisture_data_service import SensorMoistureDataService
from ..models.sensor_moisture_data_model import SensorMoistureDataModel

sensor_moisture_data_blueprint = Blueprint('sensor_moisture_data', __name__)

sensor_moisture_data_repository = SensorMoistureDataRepository(db.session)
sensor_moisture_data_service = SensorMoistureDataService(sensor_moisture_data_repository)

@sensor_moisture_data_blueprint.route('/sensor-moisture-data', methods=['GET'])
def get_sensor_moisture_data():
    data = sensor_moisture_data_service.get_all()
    return jsonify([{'id': d.id, 'sensor_id': d.sensor_id, 'moisture': d.moisture} for d in data]), 200

@sensor_moisture_data_blueprint.route('/sensor-moisture-data', methods=['POST'])
def create_sensor_moisture_data():
    moisture_data = request.json
    new_data = SensorMoistureDataModel(
        sensor_id=moisture_data.get("sensor_id"),
        moisture=moisture_data.get("moisture")
    )
    created_data = sensor_moisture_data_service.create(new_data)
    if created_data:
        return jsonify({'id': created_data.id, 'sensor_id': created_data.sensor_id, 'moisture': created_data.moisture}), 201
    else:
        return jsonify({"message": "Failed to create moisture data"}), 400

@sensor_moisture_data_blueprint.route('/sensor-moisture-data/<int:data_id>', methods=['GET'])
def get_sensor_moisture_data_by_id(data_id):
    data = sensor_moisture_data_service.get_by_id(data_id)
    if data:
        return jsonify({'id': data.id, 'sensor_id': data.sensor_id, 'moisture': data.moisture}), 200
    else:
        return jsonify({"message": "Data not found"}), 404

@sensor_moisture_data_blueprint.route('/sensor-moisture-data/<int:data_id>', methods=['PUT'])
def update_sensor_moisture_data(data_id):
    moisture_data = request.json
    data = sensor_moisture_data_service.get_by_id(data_id)
    if data:
        data.sensor_id = moisture_data.get("sensor_id")
        data.moisture = moisture_data.get("moisture")
        updated_data = sensor_moisture_data_service.update(data)
        return jsonify({'id': updated_data.id, 'sensor_id': updated_data.sensor_id, 'moisture': updated_data.moisture}), 200
    else:
        return jsonify({"message": "Data not found"}), 404

@sensor_moisture_data_blueprint.route('/sensor-moisture-data/<int:data_id>', methods=['DELETE'])
def delete_sensor_moisture_data(data_id):
    deleted_data = sensor_moisture_data_service.delete(data_id)
    if deleted_data:
        return jsonify({"message": f"Moisture data {data_id} deleted"}), 204
    else:
        return jsonify({"message": "Data not found"}), 404
