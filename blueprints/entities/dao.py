from datetime import datetime
from uuid import uuid4
from shared.page import Page


class Entity:
    def __init__(self, name=None, company=None, city=None):
        self.id = str(uuid4())
        self.name = name
        self.company = company
        self.city = city
        self.created_at = str(datetime.now())

class EntityDB:
    def __init__(self):
        self.entities = [Entity(name=str(uuid4()), company=str(uuid4()), city=str(uuid4())) for _ in range(100)]

    def create_entity(self, name, company, city) -> Entity:
        new_entity = Entity(name, company, city)
        self.entities.append(new_entity)
        return new_entity
    
    def paginate(self, page, per_page = 10) -> Page:
        start = (page - 1) * per_page
        end = start + per_page
        paginated_entities = self.entities[start:end]
        total_rows = len(self.entities)
        return Page(rows=paginated_entities, page = page, per_page = per_page, total_rows = total_rows)

    def get_entity_by_id(self, entity_id) -> Entity:
        return next(
            (entity for entity in self.entities if entity.id == entity_id), None
        )

    def update_entity(self, entity_id, name, company, city) -> Entity | None:
        entity = self.get_entity_by_id(entity_id)
        if entity:
            entity.name = name
            entity.company = company
            entity.city = city
            return entity
        return None

    def delete_entity(self, entity_id) -> bool:
        entity = self.get_entity_by_id(entity_id)
        if entity:
            self.entities.remove(entity)
            return True
        return False


entity_dao = EntityDB()
