import random

# class Forest:
#     def __init__(self):
#         self.predators = ['Tiger', 'Crocodile', 'Bear', 'Shark', 'Komodo', 'Leopard', 'Panther', 'Cobra',
#                           'Wildcat', 'Gharial', 'Eagle', 'Cheetah']
#         self.herbivorous = ['Beaver', 'Bison', 'Buffalo', 'Camel', 'Goose', 'Oriole', 'Aphid', 'Tortoise',
#                             'Rabbit', 'Iguana', 'Panda', 'Goat']
#
#         self.dict_predators = {self.predators[index]: [random.randint(25, 100), random.randint(25, 100)] for index in
#                                range(0, len(self.predators))}
#         self.dict_herbivorous = {self.herbivorous[index]: [random.randint(25, 100), random.randint(25, 100)] for index
#                                  in
#                                  range(0, len(self.herbivorous))}
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.random_of_herb = random.choice(list(self.dict_herbivorous.items()))
#         self.random_of_pred = random.choice(list(self.dict_predators.items()))
#         if random.choice([self.random_of_pred, self.random_of_herb]) == self.random_of_pred:
#             return f'Is predator: {self.random_of_pred} {type(self.random_of_pred)}'
#         else:
#             return f'Is herbivorou: {self.random_of_herb} {type(self.random_of_herb)}'
#
# dd = Forest()
# for i in dd:
#     print(i)
        # return random.choice([self.random_of_pred, self.random_of_herb])





class Forest:
    def __init__(self, num):
        self.num = num
        self.predator = ['Tiger', 'Crocodile', 'Bear', 'Shark', 'Komodo', 'Leopard', 'Panther', 'Cobra',
                          'Wildcat', 'Gharial', 'Eagle', 'Cheetah']
        self.herbivorou = ['Beaver', 'Bison', 'Buffalo', 'Camel', 'Goose', 'Oriole', 'Aphid', 'Tortoise',
                            'Rabbit', 'Iguana', 'Panda', 'Goat']

    def __iter__(self):
        return self

    def __next__(self):
        self.pred_list = [[random.choice(self.predator), random.randint(25, 100), random.randint(25, 100)] for i in
                          range(self.num)]
        self.herb_list = [[random.choice(self.herbivorou), random.randint(25, 100), random.randint(25, 100)] for i in
                          range(self.num)]
        if random.choice([self.pred_list, self.herb_list]) == self.pred_list:
            return random.choice(self.pred_list)
        else:
            return random.choice(self.herb_list)

