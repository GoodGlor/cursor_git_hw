# 1

class Laptop:
    def __init__(self):
        nickel_cadmium = Battery('Nickel Cadmium')
        nickel_metal_hydride = Battery('Nickel Metal Hydride')
        lithium_io = Battery('Lithium Io')
        self.batterys = [nickel_cadmium, nickel_metal_hydride, lithium_io]


class Battery:
    def __init__(self, types):
        self.type = types


laptop = Laptop()


# 2

class Guitar:
    def __init__(self, types_strings):
        self.types_strings = types_strings


class GuitarString:
    pass


string = GuitarString()
guitar = Guitar(string)

# 3 

class Calc:

    @staticmethod
    def add_nums(a, b, c):
        return a + b + c



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
    def visitors_count(self):
        return self._visitors_count

    @visitors_count.setter
    def visitors_count(self, new_count):
        print('seter')

        if new_count > self.max_visitors_num:
            self._visitors_count = self.max_visitors_num
        else:
            self._visitors_count = new_count



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

    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def __str__(self):
        return f'AddressBook (key= {self.key} name= {self.name} phone_number= {self.phone_number} ' \
               f'address= {self.address} email= {self.email} birthday= {self.birthday} age= {self.age}'



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
student.email = 'tema@cursor.com'
stud_email = getattr(student, 'email')
print(stud_email)


# 11

class Celsius:

    def __init__(self, temperature=0):
        self._temperature = temperature
	
    @property
    def temperature(self):
        return (self._temperature * 1.8) + 32


obj = Celsius(25)

print(obj.temperature)

