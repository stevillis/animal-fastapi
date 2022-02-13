from uuid import UUID

from fastapi import APIRouter

from data import AnimalList
from models import AnimalModel

animal_list = AnimalList()

animal_router = APIRouter()


@animal_router.get('/')
async def list_all():
    return animal_list.list_all()


@animal_router.get('/{animal_id}')
async def get_animal(animal_id: UUID):
    return animal_list.get_animal(animal_id)


@animal_router.post('/')
async def create_animal(animal: AnimalModel):
    return animal_list.insert(animal)
