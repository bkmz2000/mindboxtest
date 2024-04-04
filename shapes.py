from typing import Union, Iterable, Protocol

from math import pi


"""
Напишите на C# или Python библиотеку для поставки внешним клиентам, которая умеет вычислять площадь круга по радиусу и треугольника по трем сторонам. Дополнительно к работоспособности оценим:

[V] Юнит-тесты
[V] Легкость добавления других фигур
[X] Вычисление площади фигуры без знания типа фигуры в compile-time
[V] Проверку на то, является ли треугольник прямоугольным

1. Будем считать фигурой все, у чего есть поле `area: float`, для этого 
будем использовать соответствующий протокол. Если нужно будет добавить новую фигуру,
просто определим в ее классе это свойсто. Можно было бы использовать абстрактные классы и наследование,
но простоколы мне нравятся больше.

Функция area_sum показывает, как можно использовать этот протокол можно использовать.

2. Компайл тайма нет :)
"""

number = Union[int, float]


class Shape(Protocol):
    area: float


class Circle:
    def __init__(self, r: number) -> None:
        if not isinstance(r, (int, float)):
            raise TypeError(f"Radius must be a number, got {type(r)}")
        if r <= 0:
            raise ValueError(f"Radius must be a positive number, got {r}")

        self._r = float(r)

    @property
    def r(self) -> float:
        return self._r

    @property
    def area(self) -> float:
        return self._r**2 * pi


class Triangle:
    def __init__(self, a: number, b: number, c: number) -> None:
        for x in [a, b, c]:
            if not isinstance(x, (int, float)):
                raise TypeError(f"Sides must be a number, got {type(x)}")
            if x <= 0:
                raise ValueError(f"Sides must be positive numbers, got {x}")

        if sum([a, b, c]) <= 2*max([a, b, c]):
            raise ValueError(
                f"Sides should validate the triangle inequality, got {a}, {b}, {c}")

        # Обидно, что тайпчекер не умеет выводить tuple[float, float, float]
        self._sides = tuple(sorted(map(float, [a, b, c])))

    @property
    def is_right(self) -> bool:
        small = 0.00001
        a, b, c = self._sides
        return abs(a**2+b**2 - c**2) < small

    @property
    def sides(self) -> tuple[float, ...]:
        return self._sides

    @property
    def area(self) -> float:
        p = sum(self._sides)/2
        s_squared = p

        for side in self._sides:
            s_squared *= p-side

        return s_squared**0.5


def area_sum(shapes: Iterable[Shape]) -> float:
    ret: float = 0

    for shape in shapes:
        ret += shape.area

    return ret
