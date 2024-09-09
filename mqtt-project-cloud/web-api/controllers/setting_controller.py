from flask import Blueprint, jsonify, request
from ..extensions import db
from ..repositories.setting_repository import SettingRepository
from ..services.setting_service import SettingService

setting_blueprint = Blueprint('setting', __name__)

# Initialize repository and service
setting_repository = SettingRepository(db.session)
setting_service = SettingService(setting_repository)

# GET all settings
@setting_blueprint.route('/settings', methods=['GET'])
def get_settings():
    data = setting_service.get_all()
    return jsonify(data), 200

# POST create a new setting
@setting_blueprint.route('/settings', methods=['POST'])
def create_setting():
    setting_data = request.json
    if not setting_data.get("sensor_id"):
        return jsonify({"message": "sensor_id is required"}), 400

    created_data = setting_service.create(setting_data)
    if created_data:
        return jsonify(created_data), 201
    else:
        return jsonify({"message": "Failed to create setting"}), 400

# GET settings for a specific sensor by sensor_id
@setting_blueprint.route('/sensors/<int:sensor_id>/setting', methods=['GET'])
def get_settings_by_sensor_id(sensor_id):
    data = setting_service.get_by_sensor_id(sensor_id)
    if data:
        return jsonify(data), 200
    else:
        return jsonify({"message": "Settings not found for this sensor"}), 404

# PUT update an existing setting by sensor_id
@setting_blueprint.route('/sensors/<int:sensor_id>/setting', methods=['PUT'])
def update_setting_by_sensor_id(sensor_id):
    setting_data = request.json
    updated_data = setting_service.update_by_sensor_id(sensor_id, setting_data)
    if updated_data:
        return jsonify(updated_data), 200
    else:
        return jsonify({"message": "Settings not found for this sensor"}), 404

# DELETE a setting
@setting_blueprint.route('/settings/<int:setting_id>', methods=['DELETE'])
def delete_setting(setting_id):
    deleted_data = setting_service.delete(setting_id)
    if deleted_data:
        return '', 204  # Return 204 No Content
    else:
        return jsonify({"message": "Setting not found"}), 404
