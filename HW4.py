# 1- 4
class Vehicle:

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def characteristics(self):
        print(f'Max speed is {self.max_speed} and mileage {self.mileage}')


class Bus(Vehicle):
    def __init__(self, max_speed, mileage, seat_cap):
        self.seat_cap = seat_cap

        super().__init__(max_speed, mileage)

    def seating_capacity(self):
        print(f'My has max speed {self.max_speed}, mileage {self.mileage} and seat capacity {self.seat_cap}')


school_bus = Bus(220, 1262, '45')
print(type(Bus))
print(isinstance(school_bus, Vehicle))
print(issubclass(Bus, Vehicle))


# 5 - 6

class School:
    def __init__(self, get_school_id, number_of_students):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students


class SchoolBus(School, Bus):
    def __init__(self, max_speed, mileage, seat_cap, get_school_id, number_of_students, bus_school_color):
        self.bus_school_color = bus_school_color
        Bus.__init__(self, max_speed, mileage, seat_cap)
        School.__init__(self, get_school_id, number_of_students)

    def about_school(self):
        print(f' Max_speed is: {self.max_speed}\n Mileage is: {self.mileage}\n Seat_cap is: {self.seat_cap}\n '
              f'Get_school_id is: {self.get_school_id}\n Number_of_students is: {self.number_of_students} \n'
              f' Bus_school_color is: {self.bus_school_color}')


schobus = SchoolBus(80, 12345, 45, 0, 987, 'red')
schobus.about_school()


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
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __new__(cls, name, population):
        instanced = super(City, cls).__new__(cls)
        return instanced if population > 1500 else 'Your city is too small'

# 9
    def __str__(self):
        return f'The population of the city {self.name} is {self.population}'


city = City('Odessa', 1800)
print(city)


# 10


class Add:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num * other.num if self.num > 10 else self.num + other.num


a_1 = Add(11)
a_2 = Add(2)
a = a_1 + a_2
print(a)


# 11

class Total:
    def __call__(self, x, z):
        k = x + z
        return k


total = Total()
print(total(11,1))

# 12

class MyOrder:
    def __init__(self, cart, customer):
        self.cart = cart
        self.customer = customer

    def __bool__(self):
        if len(list(self.cart)) != 0:
            return True
        else:
            return False

    def __str__(self):
        return f'{self.cart}'


order_1 = MyOrder(['a', 'b', 'c'], 'd')
order_2 = MyOrder([], 'a')

print(bool(order_1))
print(bool(order_2))
