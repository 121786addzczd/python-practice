from typing import Annotated
from fastapi import APIRouter, Path, Query, HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status
from cruds import item as item_cruds, auth as auth_cruds
from schemas import ItemCreate, ItemUpdate, ItemResponse, DecodedToken
from database import get_db


DbDeoendency = Annotated[Session, Depends(get_db)]

router = APIRouter(prefix="/items", tags=["items"])

UserDependency = Annotated[DecodedToken, Depends(auth_cruds.get_current_user)]

@router.get("", response_model=list[ItemResponse], status_code=status.HTTP_200_OK)
async def find_all(db: DbDeoendency):
    return item_cruds.find_all(db)


@router.get("/{id}", response_model=ItemResponse, status_code=status.HTTP_200_OK)
async def find_by_id(db: DbDeoendency, id: int=Path(gt=0)):
    found_item = item_cruds.find_by_id(db, id)
    if not found_item:
        raise HTTPException(status_code=404, detail="item not found")
    return found_item


@router.get("/", response_model=list[ItemResponse], status_code=status.HTTP_200_OK)
async def find_by_name(db: DbDeoendency, name: str = Query(min_length=2, max_length=20)):
    return item_cruds.find_by_name(db, name)


@router.post("", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
async def create(db: DbDeoendency, user: UserDependency, item_create: ItemCreate):
    return item_cruds.create(db, item_create, user.user_id)


@router.put("/{id}", response_model=ItemResponse, status_code=status.HTTP_200_OK)
async def update(db: DbDeoendency, item_update: ItemUpdate, id: int=Path(gt=0)):
    updated_item = item_cruds.update(db, id, item_update)
    if not updated_item:
        raise HTTPException(status_code=404, detail="Item not updated")
    return updated_item


@router.delete("/{id}", response_model=ItemResponse, status_code=status.HTTP_200_OK)
async def delete(db: DbDeoendency, id: int=Path(gt=0)):
    deleted_item = item_cruds.delete(db, id)
    if not deleted_item:
        raise HTTPException(status_code=404, detail="Item not deleted")
    return deleted_item
