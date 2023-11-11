from sqlalchemy.orm import Session
from schemas import ItemCreate, ItemUpdate
from models import Item

def find_all(db: Session):
    return db.query(Item).all()

def find_by_id(db: Session, id: int):
    return db.query(Item).filter(Item.id == id).first()


def find_by_name(db: Session, name: str):
    return db.query(Item).filter(Item.name.like(f"%{name}%")).all()


def create(db: Session, item_create: ItemCreate):
    new_item = Item(
        **item_create.model_dump()
    )
    db.add(new_item)
    db.commit()
    return new_item


# def update(id: int, item_update: ItemUpdate):
#     for item in items:
#         if item.id == id:
#             item.name = item.name if item_update.name is None else item_update.name
#             item.price = item.price if item_update.price is None else item_update.price
#             item.description = item.description if item_update.description is None else item_update.description
#             item.status = item.status if item_update.status is None else item_update.status
#             return item
#     return None


# def delete(id: int):
#     for i in range(len(items)):
#         if items[i].id == id:
#             delete_item = items.pop(i)
#             return delete_item
#     return None