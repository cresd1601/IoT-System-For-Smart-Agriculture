from flask import Blueprint, jsonify, request
from ..extensions import db
from ..repositories.sensor_temperature_data_repository import SensorTemperatureDataRepository
from ..services.sensor_temperature_data_service import SensorTemperatureDataService
from ..models.sensor_temperature_data_model import SensorTemperatureDataModel

sensor_temperature_data_blueprint = Blueprint('sensor_temperature_data', __name__)

sensor_temperature_data_repository = SensorTemperatureDataRepository(db.session)
sensor_temperature_data_service = SensorTemperatureDataService(sensor_temperature_data_repository)

@sensor_temperature_data_blueprint.route('/sensor-temperature-data', methods=['GET'])
def get_sensor_temperature_data():
    data = sensor_temperature_data_service.get_all()
    return jsonify([{'id': d.id, 'sensor_id': d.sensor_id, 'temperature': d.temperature, 'humidity': d.humidity} for d in data]), 200

@sensor_temperature_data_blueprint.route('/sensor-temperature-data', methods=['POST'])
def create_sensor_temperature_data():
    temperature_data = request.json
    new_data = SensorTemperatureDataModel(
        sensor_id=temperature_data.get("sensor_id"),
        temperature=temperature_data.get("temperature"),
        humidity=temperature_data.get("humidity")
    )
    created_data = sensor_temperature_data_service.create(new_data)
    if created_data:
        return jsonify({'id': created_data.id, 'sensor_id': created_data.sensor_id, 'temperature': created_data.temperature, 'humidity': created_data.humidity}), 201
    else:
        return jsonify({"message": "Failed to create temperature data"}), 400

@sensor_temperature_data_blueprint.route('/sensor-temperature-data/<int:data_id>', methods=['GET'])
def get_sensor_temperature_data_by_id(data_id):
    data = sensor_temperature_data_service.get_by_id(data_id)
    if data:
        return jsonify({'id': data.id, 'sensor_id': data.sensor_id, 'temperature': data.temperature, 'humidity': data.humidity}), 200
    else:
        return jsonify({"message": "Data not found"}), 404

@sensor_temperature_data_blueprint.route('/sensor-temperature-data/<int:data_id>', methods=['PUT'])
def update_sensor_temperature_data(data_id):
    temperature_data = request.json
    data = sensor_temperature_data_service.get_by_id(data_id)
    if data:
        data.sensor_id = temperature_data.get("sensor_id")
        data.temperature = temperature_data.get("temperature")
        data.humidity = temperature_data.get("humidity")
        updated_data = sensor_temperature_data_service.update(data)
        return jsonify({'id': updated_data.id, 'sensor_id': updated_data.sensor_id, 'temperature': updated_data.temperature, 'humidity': updated_data.humidity}), 200
    else:
        return jsonify({"message": "Data not found"}), 404

@sensor_temperature_data_blueprint.route('/sensor-temperature-data/<int:data_id>', methods=['DELETE'])
def delete_sensor_temperature_data(data_id):
    deleted_data = sensor_temperature_data_service.delete(data_id)
    if deleted_data:
        return jsonify({"message": f"Temperature data {data_id} deleted"}), 204
    else:
        return jsonify({"message": "Data not found"}), 404
