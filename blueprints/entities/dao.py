from datetime import datetime
from uuid import uuid4


class Entity:
    def __init__(self, name=None, company=None, city=None):
        self.id = str(uuid4())
        self.name = name
        self.company = company
        self.city = city
        self.created_at = str(datetime.now())


class EntityDB:
    def __init__(self):
        self.entities = []

    def create_entity(self, name, company, city):
        new_entity = Entity(name, company, city)
        self.entities.append(new_entity)
        return new_entity
    
    def paginate(self, page, per_page = 10):
        start = (page - 1) * per_page
        end = start + per_page
        paginated_entities = self.entities[start:end]
        return paginated_entities

    def get_entity_by_id(self, entity_id):
        return next(
            (entity for entity in self.entities if entity.id == entity_id), None
        )

    def update_entity(self, entity_id, name, company, city):
        entity = self.get_entity_by_id(entity_id)
        if entity:
            entity.name = name
            entity.company = company
            entity.city = city
            return entity
        return None

    def delete_entity(self, entity_id):
        entity = self.get_entity_by_id(entity_id)
        if entity:
            self.entities.remove(entity)
            return True
        return False


entity_dao = EntityDB()
