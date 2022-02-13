from uuid import UUID

from fastapi import APIRouter

from data import AnimalList

animal_list = AnimalList()

animal_router = APIRouter()


@animal_router.get('/')
async def list_all():
    return animal_list.list_all()


@animal_router.get('/{animal_id}')
async def get_animal(animal_id: UUID):
    return animal_list.get_animal(animal_id)
