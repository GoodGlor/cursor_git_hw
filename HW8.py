from __future__ import annotations
import random
from typing import Dict, Any
from abc import ABC, abstractmethod

predators_list = ['Tiger', 'Crocodile', 'Bear', 'Shark', 'Komodo', 'Leopard', 'Panther', 'Cobra',
                  'Wildcat', 'Gharial', 'Eagle', 'Cheetah']
herbivorous_list = ['Beaver', 'Bison', 'Buffalo', 'Camel', 'Goose', 'Oriole', 'Aphid', 'Tortoise',
                    'Rabbit', 'Iguana', 'Panda', 'Goat']

different = {'predator': 0, 'herbivorous': 1}


class Animal(ABC):
    def __init__(self, type_animal: int, name: str, power: int, speed: int):
        self.type_animal = type_animal
        self.name = name
        self.power = power
        self.speed = speed

    @abstractmethod
    def eat(self, forest: Forest):
        pass

    @abstractmethod
    def state(self, forest: Forest):
        pass


class Herbivores(Animal):
    def __init__(self, type_animal, name, power, speed):
        super(Herbivores, self).__init__(type_animal, name, power, speed)

    def state(self, forest: Forest):
        return f'{self.name} power {self.power} speed {self.speed}'

    def eat(self, forest: Forest):
        percent = self.power * 0.5
        self.power += percent
        if self.power > 100:
            difference = self.power - 100
            self.power = self.power - difference


class Predator(Animal):
    def __init__(self, type_animal, name, power, speed):
        super(Predator, self).__init__(type_animal, name, power, speed)

    def state(self, forest: Forest):
        return f'{self.name} power {self.power} speed {self.speed}'

    def eat(self, forest: Forest):
        percent = self.power * 0.5
        self.power += percent
        if self.power > 100:
            difference = self.power - 100
            self.power = self.power - difference


AnyAnimal: Any[Herbivores, Predator]


class Forest:

    def __init__(self):
        self.animals: Dict[str, AnyAnimal] = dict()
        self.list_animals = []

    def add_animal(self, animal: AnyAnimal):
        #self.list_animals.append([dict(type_of_animal=animal.type_animal, name=animal.name, power=animal.power, speed=animal.speed)])
        self.list_animals.append([animal])

        return self.list_animals



    def remove_animal(self, animal: AnyAnimal):
        pass

    def __iter__(self):
        return self

    def __next__(self):
        return random.choice(self.list_animals)


def animal_generator():
    while True:
        predator = Predator(0, random.choice(predators_list), random.randint(25, 100), random.randint(25, 100))
        herbivore = Herbivores(1, random.choice(herbivorous_list), random.randint(25, 100),
                               random.randint(25, 100))
        yield random.choice([predator, herbivore])


nature = animal_generator()

forest = Forest()
for i in range(10):
    animal = next(nature)
    forest.add_animal(animal)

for an in forest.list_animals:
    for ani in an:
        print(ani.state(forest=forest))
        # if ani.name == ani.name:
        #     ani.





