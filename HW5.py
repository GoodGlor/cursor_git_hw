# 1

class Laptop:
    def __init__(self):
        battery_1 = Battery('Nickel Cadmium')
        battery_2 = Battery('Nickel Metal Hydride')
        battery_3 = Battery('Lithium Io')
        self.batterys = [battery_1, battery_2, battery_3]


class Battery:
    def __init__(self, type):
        self.type = type


laptop = Laptop()


# 2

class Guitar:
    def __init__(self, types):
        self.types = types


class GuitarString:
    def __init__(self):
        pass


strings_for_guitar = GuitarString()
guitar = Guitar(strings_for_guitar)

# 3

class Calc:
    def add_nums(self, a, b, c):
        total = a + b + c
        return total


obj = Calc()
print(obj.add_nums(1, 1, 1))


# 4

class Pasta:

    def __init__(self, ingredients):
        self.ingredients = ingredients

    @staticmethod
    def carbonara():
        return Pasta(['forcemeat', 'tomatoes'])

    @staticmethod
    def bolognaise():
        return Pasta(['bacon', 'parmesan', 'eggs'])


# 5

class Concert:
    max_visitors_num = 0

    def __init__(self, visitors_count=0):
        self._visitors_count = visitors_count

    @property
    def count(self):
        return self._visitors_count

    @count.setter
    def count(self, visitors_count):
        if visitors_count > self.max_visitors_num:
            self._visitors_count = self.max_visitors_num
        else:
            self._visitors_count = visitors_count


Concert.max_visitors_num = 50
concert = Concert()
concert.count = 1000
print(concert.count)

