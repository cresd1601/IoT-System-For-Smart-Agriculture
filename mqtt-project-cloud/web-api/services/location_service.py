from ..models.location_model import LocationModel  # Importing the LocationModel
from ..repositories.location_repository import LocationRepository  # Importing the repository

class LocationService:
    def __init__(self, location_repository: LocationRepository):
        self.location_repository = location_repository

    def get_all(self):
        locations = self.location_repository.get_all()
        return [
            {
                'id': location.id,
                'name': location.name,
                'address': location.address,
                'description': location.description
            } for location in locations
        ]

    def create(self, location_data):
        new_location = LocationModel(
            name=location_data.get("name"),
            address=location_data.get("address"),
            description=location_data.get("description")
        )
        created_location = self.location_repository.create(new_location)
        if created_location:
            return {
                'id': created_location.id,
                'name': created_location.name,
                'address': created_location.address,
                'description': created_location.description
            }
        return None

    def get_by_id(self, location_id):
        location = self.location_repository.get_by_id(location_id)
        if location:
            return {
                'id': location.id,
                'name': location.name,
                'address': location.address,
                'description': location.description
            }
        return None

    def update(self, location, location_data):
        location.name = location_data.get("name")
        location.address = location_data.get("address")
        location.description = location_data.get("description")
        updated_location = self.location_repository.update(location)
        if updated_location:
            return {
                'id': updated_location.id,
                'name': updated_location.name,
                'address': updated_location.address,
                'description': updated_location.description
            }
        return None

    def delete(self, location_id):
        return self.location_repository.delete(location_id)
