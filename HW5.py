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
