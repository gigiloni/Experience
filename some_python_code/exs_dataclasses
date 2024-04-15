from dataclasses import dataclass, field, InitVar, make_dataclass
from typing import Any


class Vector3D:
    def __init__(self, x: int, y: int, z: int, calc_len: bool = True):
        self.x = x
        self.y = y
        self.z = z
        self.length = (x * x + y * y + z * z) ** 0.5 if calc_len else 0


@dataclass(eq=True, order=True)
class V3D:
    x: int = field(repr=False)
    y: int
    z: int = field(compare=False)
    calc_len: InitVar[bool] = True
    length: float = field(init=False, compare=False, default=0)

    def __post_init__(self, calc_len: bool):
        if calc_len:
            self.length = (self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5


v = V3D(1, 2, 3)
v2 = V3D(1, 2, 5, False)
print(v, v.__dict__, v2)


class GoodsMethodsFactory:
    @staticmethod
    def get_init_measure():
        return [0, 0, 0]


@dataclass
class Goods:
    current_uid = 0
    uid: int = field(init=False)
    price: Any = None
    weight: Any = None

    def __post_init__(self):
        Goods.current_uid += 1
        self.uid = Goods.current_uid


@dataclass
class Book(Goods):
    title: str = ""
    author: str = ""
    price: float = 0
    weight: int | float = 0
    measure: list = field(default_factory=GoodsMethodsFactory.get_init_measure)

    def __post_init__(self):
        super().__post_init__()


b = Book(10, 100, "Book1", 'Mozart')
print(b)


class Car:
"""Just use a decorator man"""
    def __init__(self, model, max_speed, price):
        self.model = model
        self.max_speed = max_speed
        self.price = price

    def get_max_speed(self):
        return self.max_speed


CarData = make_dataclass('CarData', [('model', str),
                                     'max_speed', ('price', float, field(default=0))],
                         namespace={'get_max_speed': lambda self: self.max_speed})

c = CarData('BMW', 256, 42000)
print(c, c.get_max_speed())


@dataclass
class ThingData:
    name: str
    weight: int = 0
    price: float = 0
    dims: list = field(default_factory=list)

    def __gt__(self, other):
        return self.price > other.price

    def __lt__(self, other):
        return self.price < other.price
        

td1 = ThingData('Book2', 115, 18)
td2 = ThingData('Book3', 200, 25)

print(td1 == td2)
print(td1 < td2)
