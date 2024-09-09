class BaseService:
    def __init__(self, repository):
        self.repository = repository

    def get_all(self):
        try:
            return self.repository.get_all()
        except Exception as e:
            # Log the error and handle it accordingly
            print(f"Error fetching all entities: {e}")
            return None

    def get_by_id(self, entity_id):
        try:
            entity = self.repository.get_by_id(entity_id)
            if not entity:
                raise ValueError(f"Entity with ID {entity_id} not found")
            return entity
        except Exception as e:
            # Log the error and handle it accordingly
            print(f"Error fetching entity by ID {entity_id}: {e}")
            return None

    def create(self, entity):
        try:
            created_entity = self.repository.create(entity)
            if not created_entity:
                raise ValueError("Failed to create entity")
            return created_entity
        except Exception as e:
            # Log the error and handle it accordingly
            print(f"Error creating entity: {e}")
            return None

    def update(self, entity):
        try:
            updated_entity = self.repository.update(entity)
            if not updated_entity:
                raise ValueError("Failed to update entity")
            return updated_entity
        except Exception as e:
            # Log the error and handle it accordingly
            print(f"Error updating entity: {e}")
            return None

    def delete(self, entity_id):
        try:
            entity = self.repository.get_by_id(entity_id)
            if entity:
                self.repository.delete(entity)
                return entity
            else:
                raise ValueError(f"Entity with ID {entity_id} not found")
        except Exception as e:
            # Log the error and handle it accordingly
            print(f"Error deleting entity by ID {entity_id}: {e}")
            return None
