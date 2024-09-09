from flask import Blueprint, jsonify, request
from ..extensions import db
from ..repositories.location_repository import LocationRepository
from ..services.location_service import LocationService

# Initialize the blueprint
location_blueprint = Blueprint('location', __name__)

# Initialize the repository and service
location_repository = LocationRepository(db.session)
location_service = LocationService(location_repository)

# GET all locations
@location_blueprint.route('/locations', methods=['GET'])
def get_locations():
    data = location_service.get_all()
    return jsonify(data), 200

# POST create a new location
@location_blueprint.route('/locations', methods=['POST'])
def create_location():
    location_data = request.json
    created_data = location_service.create(location_data)
    if created_data:
        return jsonify(created_data), 201
    else:
        return jsonify({"message": "Failed to create location"}), 400

# GET a specific location by ID
@location_blueprint.route('/locations/<int:location_id>', methods=['GET'])
def get_location_by_id(location_id):
    data = location_service.get_by_id(location_id)
    if data:
        return jsonify(data), 200
    else:
        return jsonify({"message": "Location not found"}), 404

# PUT update an existing location by ID
@location_blueprint.route('/locations/<int:location_id>', methods=['PUT'])
def update_location(location_id):
    location_data = request.json
    existing_data = location_service.get_by_id(location_id)
    if existing_data:
        updated_data = location_service.update(existing_data, location_data)
        if updated_data:
            return jsonify(updated_data), 200
        else:
            return jsonify({"message": "Failed to update location"}), 400
    else:
        return jsonify({"message": "Location not found"}), 404

# DELETE a specific location by ID
@location_blueprint.route('/locations/<int:location_id>', methods=['DELETE'])
def delete_location(location_id):
    deleted_data = location_service.delete(location_id)
    if deleted_data:
        return jsonify({"message": f"Location {location_id} deleted"}), 204
    else:
        return jsonify({"message": "Location not found"}), 404
