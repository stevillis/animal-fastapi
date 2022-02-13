from typing import List
from uuid import UUID, uuid4

from fastapi import HTTPException

from models import AnimalModel, AnimalUpdateModel, SexEnum


class AnimalList:
    animal_list: List[AnimalModel] = [
        AnimalModel(
            id=uuid4(),
            name="Michael",
            age=4,
            sex=SexEnum.male,
            color="white"
        ),
        AnimalModel(
            id=uuid4(),
            name="Bella",
            age=1,
            sex=SexEnum.female,
            color="gray"
        ),
    ]

    def __get_animal_by_id(self, animal_id):
        animal = filter(lambda x: x.id == animal_id, self.animal_list)
        if animal:
            return list(animal)[0]
        return HTTPException(
            status_code=404,
            detail=f'Animal with id {animal_id} does not exist'
        )

    def list_all(self):
        return self.animal_list

    def get_animal(self, animal_id) -> AnimalModel:
        return self.__get_animal_by_id(animal_id)

    def insert(self, animal: AnimalModel) -> AnimalModel:
        animal.id = uuid4()
        self.animal_list.append(animal)
        return animal

    def update(self, animal_id: UUID,
               animal_update: AnimalUpdateModel) -> AnimalModel:
        animal = self.__get_animal_by_id(animal_id)
        if animal_update.name is not None:
            animal.name = animal_update.name
        if animal_update.age is not None:
            animal.age = animal_update.age
        if animal_update.sex is not None:
            animal.sex = animal_update.sex
        if animal_update.color is not None:
            animal.color = animal_update.color
        return animal
