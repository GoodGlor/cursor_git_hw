from __future__ import annotations
import random
from typing import Dict, Any
from abc import ABC, abstractmethod
import time
import uuid

predators_list = ['Tiger', 'Crocodile', 'Bear', 'Shark', 'Komodo', 'Leopard', 'Panther', 'Cobra',
                  'Wildcat', 'Gharial', 'Eagle', 'Cheetah']
herbivorous_list = ['Beaver', 'Bison', 'Buffalo', 'Camel', 'Goose', 'Oriole', 'Aphid', 'Tortoise',
                    'Rabbit', 'Iguana', 'Panda', 'Goat']

different = {'predator': 0, 'herbivorous': 1}

AnyAnimal: Any[Herbivores, Predator]


class Animal(ABC):
    def __init__(self, name: str, power: int, speed: int):
        self.id = None
        self.name = name
        self.power = power
        self.speed = speed

    @abstractmethod
    def eat(self, forest: Forest):
        pass

    @abstractmethod
    def state(self, animal: AnyAnimal):
        pass


class Herbivores(Animal):
    def __init__(self, name, power, speed):
        super(Herbivores, self).__init__(name, power, speed)

    def state(self, forest: Forest):
        return f'{self.name} power {self.power} speed {self.speed}'

    def eat(self, forest: Forest):
        print(f'Eating {self.name} ')
        percent = self.power * 0.5
        self.power += round(percent)
        if self.power > 100:
            difference = self.power - 100
            self.power = self.power - difference


class Predator(Animal):
    def __init__(self, name, power, speed):
        super(Predator, self).__init__(name, power, speed)

    def state(self, forest: Forest):
        return f'{self.name} power {self.power} speed {self.speed}'

    def eat(self, forest: Forest):
        for one in forest.animals.values():
            if one.id == self.id:
                return False
            print(f'{self.name} fight with {one.name}')
            if one.speed > self.speed:
                self.power = self.power - (round(self.power*0.3))
                return False
            elif one.power > self.power:
                self.power = self.power - (round(self.power * 0.3))



class Forest:

    def __init__(self):
        self.animals: Dict[str, AnyAnimal] = dict()

    def add_animal(self, animal: AnyAnimal):
        return self.animals.update({animal.id: animal})

    def remove_animal(self):
        pass

    def any_predator(self):
        pass

    def __iter__(self):
        return self

    def __next__(self):
        return self.animals


def animal_generator():
    while True:
        any_animal = random.choice(
            (Predator(random.choice(predators_list), random.randint(25, 100), random.randint(25, 100)),
             Herbivores(random.choice(herbivorous_list), random.randint(25, 100), random.randint(25, 100))))
        any_animal.id = uuid.uuid4()
        yield any_animal


nature = animal_generator()

forest = Forest()
for i in range(2):
    animal = next(nature)
    forest.add_animal(animal)
print(forest.animals.values())

while True:
    for x in forest.animals.values():
        x.eat(forest=forest)
        print(x.state(forest=forest))
    time.sleep(2)






