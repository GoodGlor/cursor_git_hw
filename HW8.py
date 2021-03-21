from __future__ import annotations
import random
from typing import Dict, Any
from abc import ABC, abstractmethod
import time
import uuid

predators_list = ['Tiger', 'Crocodile', 'Bear', 'Komodo', 'Leopard', 'Panther', 'Cobra',
                  'Wildcat', 'Gharial', 'Eagle', 'Cheetah']
herbivorous_list = ['Beaver', 'Bison', 'Buffalo', 'Goose', 'Oriole', 'Aphid', 'Tortoise',
                    'Rabbit', 'Iguana', 'Panda', 'Goat']

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
        print(f'{self.name} eating grass ')
        self.power += round(self.power * 0.5)
        if self.power > 100:
            self.power -= (self.power - 100)


class Predator(Animal):
    def __init__(self, name, power, speed):
        super(Predator, self).__init__(name, power, speed)

    def state(self, forest: Forest):
        return f'{self.name} power {self.power} speed {self.speed}'

    def eat(self, forest: Forest):
        predator_choose = random.choice(list(forest.animals.values()))

        if predator_choose.id == self.id:
            return False
        if predator_choose.speed > self.speed:
            print('Did not catch up prey')
            self.power -= (round(self.power * 0.3))
            predator_choose.power -= round(predator_choose.power * 0.3)
            return False
        if self.speed > predator_choose.speed:
            if self.power > predator_choose.power:
                print(f'{self.name} fight with {predator_choose.name}')
                predator_choose.power -= round(predator_choose.power * 0.3)
                self.power += (round(self.power * 0.5))
                if self.power > 100:
                    self.power -= (self.power - 100)
            else:
                self.power -= (round(self.power * 0.3))
        else:
            return False


class Forest:

    def __init__(self):
        self.animals: Dict[str, AnyAnimal] = dict()

    def add_animal(self, animal: AnyAnimal):
        return self.animals.update({animal.id: animal})

    def remove_animal(self, animal: AnyAnimal):
        return self.animals.pop(animal)

    def any_predator(self):
        check = [False if isinstance(predator, Predator) else True for predator in self.animals.values()]
        return all(check)

    def all_state(self):
        predators = 0
        herbivorus = 0
        for calculate in self.animals.values():
            if isinstance(calculate, Predator):
                predators += 1
            else:
                herbivorus += 1
        return f'In forest {predators} predators an {herbivorus} herbivores and such animals ' \
               f'{[stat.state(forest=forest) for stat in self.animals.values()]}'

    def __iter__(self):
        return self

    def __next__(self):
        random_animal = random.choice(list(self.animals.values()))
        check = [False if isinstance(predator, Predator) else True for predator in self.animals.values()]
        if all(check):
            raise StopIteration
        return random_animal


def animal_generator():
    while True:
        any_animal = random.choice(
            (Predator(random.choice(predators_list), random.randint(25, 100), random.randint(25, 100)),
             Herbivores(random.choice(herbivorous_list), random.randint(25, 100), random.randint(25, 100))))
        any_animal.id = uuid.uuid4()
        yield any_animal


nature = animal_generator()
forest = Forest()

for i in range(10):
    animal = next(nature)
    forest.add_animal(animal)

while True:
    if forest.any_predator():
        break
    for animals in forest:
        if animals.power <= 1:
            forest.remove_animal(animals.id)
        animals.eat(forest=forest)
        print(forest.all_state())
    time.sleep(1)
