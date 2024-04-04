from random import randint
from unittest import TestCase
from shapes import *


class TestCircle(TestCase):
    def test_init(self):
        with self.assertRaises(TypeError) as cm:
            Circle("-10")

        self.assertEqual(str(cm.exception),
                         "Radius must be a number, got <class 'str'>")

        with self.assertRaises(ValueError) as cm:
            Circle(-10)

        self.assertEqual(str(cm.exception),
                         "Radius must be a positive number, got -10")

    def test_area(self):
        # На всякий случай, в этой задаче, скорее всего, можно было бы и на равенство проверять
        small = 0.00001

        for _ in range(100):
            r = randint(1, 100) / randint(1, 100)
            self.assertLess(abs(Circle(r).area - r**2 * pi), small)


class TestTriangle(TestCase):
    def test_init(self):
        with self.assertRaises(TypeError) as cm:
            Triangle(1, 2, '3')

        self.assertEqual(str(cm.exception),
                         "Sides must be a number, got <class 'str'>")

        with self.assertRaises(TypeError) as cm:
            Triangle(1, '2', 3)

        self.assertEqual(str(cm.exception),
                         "Sides must be a number, got <class 'str'>")

        with self.assertRaises(TypeError) as cm:
            Triangle('1', 2, 3)

        self.assertEqual(str(cm.exception),
                         "Sides must be a number, got <class 'str'>")

        with self.assertRaises(ValueError) as cm:
            Triangle(-1, 2, 3)

        self.assertEqual(str(cm.exception),
                         "Sides must be positive numbers, got -1")

        with self.assertRaises(ValueError) as cm:
            Triangle(1, 1, 100)

        self.assertEqual(str(cm.exception),
                         "Sides should validate the triangle inequality, got 1, 1, 100")

    def test_area(self):
        small = 0.00001

        for _ in range(100):
            a = randint(1, 100)/randint(1, 100)
            b = randint(1, 100)/randint(1, 100)
            c = randint(1, 100)/randint(1, 100)

            p = (a+b+c)/2
            s = (p*(p-a)*(p-b)*(p-c))**0.5

            if sum([a, b, c]) > 2*max([a, b, c]):
                self.assertLess(Triangle(a, b, c).area-s, small,
                                f"{Triangle(a, b, c).area}, {s}, {a}, {b}, {c}")

    def test_is_right(self):
        for _ in range(100):
            a = randint(1, 100)/randint(1, 100)
            b = randint(1, 100)/randint(1, 100)
            c = (a**2+b**2)**0.5

            self.assertTrue(Triangle(a, c, b).is_right, f"{a} {b} {c}")

        for _ in range(100):
            a = randint(1, 100)/randint(1, 100)
            b = randint(1, 100)/randint(1, 100)
            c = (a**2+b**2)**0.5+1

            if sum([a, b, c]) > 2*max([a, b, c]):
                self.assertFalse(Triangle(a, c, b).is_right)
