from flask import Blueprint, jsonify, request
from ..extensions import db
from ..repositories.setting_repository import SettingRepository
from ..services.setting_service import SettingService
from ..models.setting_model import SettingModel

setting_blueprint = Blueprint('setting', __name__)

setting_repository = SettingRepository(db.session)
setting_service = SettingService(setting_repository)

@setting_blueprint.route('/settings', methods=['GET'])
def get_settings():
    data = setting_service.get_all()
    return jsonify([
        {
            'id': d.id,
            'sensor_id': d.sensor_id,
            'max_temperature': d.max_temperature,
            'min_temperature': d.min_temperature,
            'max_humidity': d.max_humidity,
            'min_humidity': d.min_humidity,
            'max_moisture': d.max_moisture,
            'min_moisture': d.min_moisture
        } for d in data
    ]), 200

@setting_blueprint.route('/settings', methods=['POST'])
def create_setting():
    setting_data = request.json
    new_data = SettingModel(
        sensor_id=setting_data.get("sensor_id"),
        max_temperature=setting_data.get("max_temperature"),
        min_temperature=setting_data.get("min_temperature"),
        max_humidity=setting_data.get("max_humidity"),
        min_humidity=setting_data.get("min_humidity"),
        max_moisture=setting_data.get("max_moisture"),
        min_moisture=setting_data.get("min_moisture")
    )
    created_data = setting_service.create(new_data)
    if created_data:
        return jsonify({
            'id': created_data.id,
            'sensor_id': created_data.sensor_id,
            'max_temperature': created_data.max_temperature,
            'min_temperature': created_data.min_temperature,
            'max_humidity': created_data.max_humidity,
            'min_humidity': created_data.min_humidity,
            'max_moisture': created_data.max_moisture,
            'min_moisture': created_data.min_moisture
        }), 201
    else:
        return jsonify({"message": "Failed to create setting"}), 400

@setting_blueprint.route('/settings/<int:setting_id>', methods=['GET'])
def get_setting_by_id(setting_id):
    data = setting_service.get_by_id(setting_id)

    if data:
        return jsonify({
            'id': data.id,
            'sensor_id': data.sensor_id,
            'max_temperature': data.max_temperature,
            'min_temperature': data.min_temperature,
            'max_humidity': data.max_humidity,
            'min_humidity': data.min_humidity,
            'max_moisture': data.max_moisture,
            'min_moisture': data.min_moisture
        }), 200
    else:
        return jsonify({"message": "Setting not found"}), 404

@setting_blueprint.route('/settings/<int:setting_id>', methods=['PUT'])
def update_setting(setting_id):
    setting_data = request.json
    data = setting_service.get_by_id(setting_id)
    if data:
        data.sensor_id = setting_data.get("sensor_id")
        data.max_temperature = setting_data.get("max_temperature")
        data.min_temperature = setting_data.get("min_temperature")
        data.max_humidity = setting_data.get("max_humidity")
        data.min_humidity = setting_data.get("min_humidity")
        data.max_moisture = setting_data.get("max_moisture")
        data.min_moisture = setting_data.get("min_moisture")
        updated_data = setting_service.update(data)
        return jsonify({
            'id': updated_data.id,
            'sensor_id': updated_data.sensor_id,
            'max_temperature': updated_data.max_temperature,
            'min_temperature': updated_data.min_temperature,
            'max_humidity': updated_data.max_humidity,
            'min_humidity': updated_data.min_humidity,
            'max_moisture': updated_data.max_moisture,
            'min_moisture': updated_data.min_moisture
        }), 200
    else:
        return jsonify({"message": "Setting not found"}), 404

@setting_blueprint.route('/settings/<int:setting_id>', methods=['DELETE'])
def delete_setting(setting_id):
    deleted_data = setting_service.delete(setting_id)
    if deleted_data:
        return jsonify({"message": f"Setting {setting_id} deleted"}), 204
    else:
        return jsonify({"message": "Setting not found"}), 404
