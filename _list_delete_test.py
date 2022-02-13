class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} - {self.age}'

    def __repr__(self):
        return f'{self.name} - {self.age}'


class AnimalList:
    def __init__(self):
        self.__animal_list = [
            Animal(name="John", age=2),
            Animal(name="Bella", age=4),
        ]

    @property
    def animal_list(self):
        return self.__animal_list


animals = AnimalList()

john = animals.animal_list[0]
print(john)

animals.animal_list.remove(john)
print(animals.animal_list)
