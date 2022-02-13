from fastapi import APIRouter

from data import AnimalList

animal_list = AnimalList()

animal_router = APIRouter()


@animal_router.get('/')
def list_all():
    return animal_list.list_all()
