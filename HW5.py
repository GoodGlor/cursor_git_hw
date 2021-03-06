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

# 6
import dataclasses


@dataclasses.dataclass
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int


# 7

import collections

AdsBDataClass = collections.namedtuple('AddressBookDataClass', {'key', 'name', 'phone_number', 'address',
                                                                'email', 'birthday', 'age'})


# 8

class AddressBook:

    def __init__(self, key=None, name=None, phone_number=None, address=None, email=None, birthday=None, age=None):

        self.__key = key
        self.__name = name
        self.__phone_number = phone_number
        self.__address = address
        self.__email = email
        self.__birthday = birthday
        self.__age = age

    @property
    def key(self):
        return self.__key

    @property
    def name(self):
        return self.__name

    @property
    def phone_number(self):
        return self.__phone_number

    @property
    def address(self):
        return self.__address

    @property
    def email(self):
        return self.__email

    @property
    def birthday(self):
        return self.__birthday

    @property
    def age(self):
        return self.__age

    @key.setter
    def key(self, x):
        if not isinstance(x, str):
            return False
        else:
            self.__key = x

    @address.setter
    def address(self, x):
        if not isinstance(x, str):
            return False
        else:
            self.__address = x

    @email.setter
    def email(self, x):
        if not isinstance(x, str):
            return False
        else:
            self.__email = x

    @birthday.setter
    def birthday(self, x):
        if not isinstance(x, str):
            return False
        else:
            self.__birthday = x

    @age.setter
    def age(self, x):
        if not isinstance(x, str):
            return False
        else:
            self.__age = x


# 9
class Person:
    name = "John"
    age = 36
    country = "USA"


person = Person()

setattr(person, 'age', 10)
print(person.age)


# 10

class Student:
    id = 0
    name = ""

    def __init__(self, id, name):
        self.id = id
        self.name = name


student = Student(10, 'Anna')

setattr(student, 'email', 'anna@cursor.com')
setattr(student, 'student_email', 'jojo@cursor.com')
print(getattr(student, 'student_email'))


# 11

class Celsius:

    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, x):
        self._temperature = (x * 1.8) + 32


obj = Celsius()
obj.temperature = 20
print(obj.temperature)

