# 1- 4
class Vehicle:

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def characteristics(self):
        print(f'Max speed is {self.max_speed} and mileage {self.mileage}')


class Bus(Vehicle):
    def __init__(self, max_speed, mileage, seat_cap):
        self.max_speed = max_speed
        self.mileage = mileage
        self.seat_cap = seat_cap

        super().__init__(max_speed, mileage)

    def seating_capacity(self):
        print(f'My has max speed {self.max_speed}, mileage {self.mileage} and seat capacity {self.seat_cap}')


School_bus = Bus(220, 1262, '45')
School_bus.seating_capacity()


# 5 - 6

class School:
    def __init__(self, get_school_id, number_of_students):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students

    def lnu(self):
        print(f'Your school id is {self.get_school_id} and your school have {self.number_of_students} students')


class SchoolBus(School):
    def __init__(self, get_school_id, number_of_students, bus_school_color):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students
        self.bus_school_color = bus_school_color
        super().__init__(get_school_id, number_of_students)

    def about_school(self):
        print(
            f'Id school is {self.get_school_id} in your school {self.number_of_students} and '
            f'this school has {self.bus_school_color} color')


zosh = SchoolBus(1, 431, 'red')
zosh.lnu()
zosh.about_school()


# 7

class Bear:
    def __init__(self, name):
        self.name = name

    def about_me(self):
        print(f"I'm bear my name is {self.name} ")

    def sound(self):
        print('AeAe')


class Wolf():
    def __init__(self, name):
        self.name = name

    def about_me(self):
        print(f"I'm wolf my name is {self.name} ")

    def sound(self):
        print('Auf')


jojo = Bear('Jojo')
dio = Wolf('Dio')

for animals in (jojo, dio):
    animals.about_me()
    animals.sound()

# 8

class City:
    def __init__(self, name, ):
        pass

