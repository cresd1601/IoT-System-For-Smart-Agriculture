class BaseRepository:
    def __init__(self, model, db_session):
        self.model = model
        self.db_session = db_session

    def get_all(self):
        return self.db_session.query(self.model).all()

    def get_by_id(self, id):
        return self.db_session.get(self.model, id)

    def create(self, entity):
        try:
            self.db_session.add(entity)
            self.db_session.commit()
            return entity
        except Exception as e:
            self.db_session.rollback()
            print(f"Error creating entity: {e}")
            return None

    def update(self, entity):
        try:
            self.db_session.merge(entity)
            self.db_session.commit()
            return entity
        except Exception as e:
            self.db_session.rollback()
            print(f"Error updating entity: {e}")
            return None

    def delete(self, entity):
        try:
            self.db_session.delete(entity)
            self.db_session.commit()
        except Exception as e:
            self.db_session.rollback()
            print(f"Error deleting entity: {e}")
            return None
