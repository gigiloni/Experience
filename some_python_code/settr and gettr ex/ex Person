from string import ascii_letters
import json


class Person:
    S_RUS = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя-'
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, name, age, ps, weight):
        self.verify_name(name=name)

        self.__name = name.split()
        self.age = age
        self.ps = ps
        self.weight = weight

    @classmethod
    def verify_name(cls, name):
        if not isinstance(name, str):
            raise TypeError('Name must be a string')

        n = name.split()
        if len(n) != 2:
            raise TypeError('Invalid name format')

        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        for s in n:
            if len(s) < 1:
                raise ValueError('The name must be have at least an one symbol')
            if len(s.strip(letters)) != 0:
                raise TypeError('You should use only a letters and dashes')

    @classmethod
    def verify_age(cls, age):
        if not isinstance(age, int) or age < 14 or age > 120:
            raise TypeError('Your old must be a number and between 14 and 120')

    @classmethod
    def verify_weight(cls, weight):
        if not isinstance(weight, float) or weight < 20:
            raise TypeError('Your weight must be a float and more than 20 kilograms')

    @classmethod
    def verify_ps(cls, ps):
        if not isinstance(ps, str):
            raise TypeError('The passport format must be a string')

        s = ps.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise ValueError('Invalid format passport')

        for n in s:
            if not n.isdigit():
                raise ValueError('Series and passport number must be numbers')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.verify_name(name=name)
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.verify_age(age=age)
        self.__age = age

    @property
    def ps(self):
        return self.__ps

    @ps.setter
    def ps(self, ps):
        self.verify_ps(ps=ps)
        self.__ps = ps

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight=weight)
        self.__weight = weight


p1 = Person(name='George Arrow', age=18, ps='1111 222222', weight=61.2)
p2 = Person(name='Alice Smith', age=21, ps='2222 222222', weight=52.1)

data = p1.__dict__, p2.__dict__

print(data)

with open('persons.json', 'w') as file:
    json.dump(data, file, indent=4)
    
