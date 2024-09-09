from flask import Blueprint, jsonify, request
from ..extensions import db
from ..repositories.location_repository import LocationRepository
from ..services.location_service import LocationService
from ..models.location_model import LocationModel

location_blueprint = Blueprint('location', __name__)

location_repository = LocationRepository(db.session)
location_service = LocationService(location_repository)

@location_blueprint.route('/locations', methods=['GET'])
def get_locations():
    data = location_service.get_all()
    return jsonify([
        {
            'id': d.id,
            'name': d.name,
            'address': d.address,
            'description': d.description
        } for d in data
    ]), 200

@location_blueprint.route('/locations', methods=['POST'])
def create_location():
    location_data = request.json
    new_data = LocationModel(
        name=location_data.get("name"),
        address=location_data.get("address"),
        description=location_data.get("description")
    )
    created_data = location_service.create(new_data)
    if created_data:
        return jsonify({
            'id': created_data.id,
            'name': created_data.name,
            'address': created_data.address,
            'description': created_data.description
        }), 201
    else:
        return jsonify({"message": "Failed to create location"}), 400

@location_blueprint.route('/locations/<int:location_id>', methods=['GET'])
def get_location_by_id(location_id):
    data = location_service.get_by_id(location_id)
    if data:
        return jsonify({
            'id': data.id,
            'name': data.name,
            'address': data.address,
            'description': data.description
        }), 200
    else:
        return jsonify({"message": "Location not found"}), 404

@location_blueprint.route('/locations/<int:location_id>', methods=['PUT'])
def update_location(location_id):
    location_data = request.json
    data = location_service.get_by_id(location_id)
    if data:
        data.name = location_data.get("name")
        data.address = location_data.get("address")
        data.description = location_data.get("description")
        updated_data = location_service.update(data)
        if updated_data:
            return jsonify({
                'id': updated_data.id,
                'name': updated_data.name,
                'address': updated_data.address,
                'description': updated_data.description
            }), 200
        else:
            return jsonify({"message": "Failed to update location"}), 400
    else:
        return jsonify({"message": "Location not found"}), 404

@location_blueprint.route('/locations/<int:location_id>', methods=['DELETE'])
def delete_location(location_id):
    deleted_data = location_service.delete(location_id)
    if deleted_data:
        return jsonify({"message": f"Location {location_id} deleted"}), 204
    else:
        return jsonify({"message": "Location not found"}), 404
