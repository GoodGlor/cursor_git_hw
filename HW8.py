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
        print(f'Eating grass {self.name} ')
        self.power += round(self.power * 0.5)
        if self.power > 100:
            self.power -= (self.power - 100)


class Predator(Animal):
    def __init__(self, name, power, speed):
        super(Predator, self).__init__(name, power, speed)

    def state(self, forest: Forest):
        return f'{self.name} power {self.power} speed {self.speed}'

    def eat(self, forest: Forest):
        # choose_anml = random.choice(list(forest.animals.values()))


        if choose_anml.id == self.id:
            return False
        print(f'---- {self.name} Found {choose_anml.name} ----')
        if choose_anml.speed > self.speed:
            print('Did not catch up')
            self.power -= (round(self.power * 0.3))
            choose_anml.power -= round(choose_anml.power * 0.3)
            return False
        if choose_anml.power <= 1:
            forest.remove_animal()
        if self.power <= 1:
            forest.remove_animal()
        if self.speed > choose_anml.speed:
            if self.power > choose_anml.power:
                print(f'{self.name} fight with {choose_anml.name}')
                choose_anml.power -= round(choose_anml.power * 0.3)
                self.power += (round(self.power * 0.5))
                if self.power > 100:
                    self.power -= (self.power - 100)
            else:
                self.power -= (round(self.power * 0.3))
            if choose_anml.power <= 1:
                forest.remove_animal()
            if self.power <= 1:
                forest.remove_animal()
        else:
            return False


class Forest:

    def __init__(self):
        self.animals: Dict[str, AnyAnimal] = dict()

    def add_animal(self, animal: AnyAnimal):
        return self.animals.update({animal.id: animal})

    def remove_animal(self):
        return self.animals.pop(animal.id)

    def any_predator(self):
        chek = [False if isinstance(x, Predator) else True for x in self.animals.values()]
        return all(chek)

    def all_state(self):
        predators = 0
        herbivorus = 0
        for x in self.animals.values():
            if isinstance(x, Predator):
                predators+=1
            else:
                herbivorus+=1

        return f'In forest {predators} predators an {herbivorus} herbivores and such animals ' \
               f'{[stat.state(forest=forest) for stat in self.animals.values()]}'

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
for i in range(6):
    animal = next(nature)
    forest.add_animal(animal)
while True:
    if forest.any_predator():
        break
    for x in forest.animals.values():
        x.eat(forest=forest)
        print(forest.all_state())

    time.sleep(1)
