import random


# class Forest:
#     predators = ['Tiger', 'Crocodile', 'Bear', 'Shark', 'Komodo', 'Leopard', 'Panther', 'Cobra',
#                  'Wildcat', 'Gharial', 'Eagle', 'Cheetah']
#
#     herbivorous = ['Beaver', 'Bison', 'Buffalo', 'Camel', 'Goose', 'Oriole', 'Aphid', 'Tortoise',
#                    'Rabbit', 'Iguana', 'Panda', 'Goat']
#
# #
# #     def dict(self):
#         self.dict_predators = {self.predators[index]: [random.randint(25, 100), random.randint(25, 100)] for index in
#                                range(0, len(self.predators))}
#         self.dict_herbivorous = {self.herbivorous[index]: [random.randint(25, 100), random.randint(25, 100)] for index
#                                  in
#                                  range(0, len(self.herbivorous))}
#         self.random_of_herb = random.choice(list(self.dict_herbivorous.items()))
#         self.random_of_pred = random.choice(list(self.dict_predators.items()))
#
#         return random.choice([self.random_of_pred, self.random_of_herb])


class IterAnimal:
    def __init__(self):
        self.predators = ['Tiger', 'Crocodile', 'Bear', 'Shark', 'Komodo', 'Leopard', 'Panther', 'Cobra',
                          'Wildcat', 'Gharial', 'Eagle', 'Cheetah']
        self.herbivorous = ['Beaver', 'Bison', 'Buffalo', 'Camel', 'Goose', 'Oriole', 'Aphid', 'Tortoise',
                            'Rabbit', 'Iguana', 'Panda', 'Goat']

        self.dict_predators = {self.predators[index]: [random.randint(25, 100), random.randint(25, 100)] for index in
                               range(0, len(self.predators))}
        self.dict_herbivorous = {self.herbivorous[index]: [random.randint(25, 100), random.randint(25, 100)] for index
                                 in
                                 range(0, len(self.herbivorous))}
        self.random_of_herb = random.choice(list(self.dict_herbivorous.items()))
        self.random_of_pred = random.choice(list(self.dict_predators.items()))

    def __iter__(self):
        return self

    def __next__(self):
        # return random.choice([self.random_of_pred, self.random_of_herb])
        return self.random_of_herb



ddd = IterAnimal()




for i in ddd:
    print(i)
