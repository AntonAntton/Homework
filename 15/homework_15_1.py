from math import sqrt


class Rectangle:

    def __init__(self, width: float, height: float) -> None:
        """
        Ініціалізація прямокутника.
        """
        self.width = width
        self.height = height

    def get_square(self) -> float:
        """
        Обчислює площу прямокутника.
        """
        square = self.width * self.height
        print(f"Area: {square}")
        return square

    def __eq__(self, other: object) -> bool:
        """
        Перевизначає оператор рівності (==) для порівняння площ прямокутників.
        """
        if isinstance(other, Rectangle):
            result = self.get_square() == other.get_square()
            print(f"Equality check: {result}")
            return result
        return False

    def __add__(self, other: "Rectangle") -> "Rectangle":
        """
        Перевизначає оператор додавання (+) для створення нового прямокутника.
        """
        if isinstance(other, Rectangle):
            new_square = self.get_square() + other.get_square()
            new_side = sqrt(new_square)
            result = Rectangle(new_side, new_square / new_side)
            print(f"Sum: {result}")
            return result
        raise TypeError("Can only add objects of class Rectangle")

    def __mul__(self, n: float) -> "Rectangle":
        """
        Перевизначає оператор множення (*) на число.
        """
        if isinstance(n, (int, float)) and n > 0:
            new_square = self.get_square() * n
            new_side = sqrt(new_square)
            result = Rectangle(new_side, new_square / new_side)
            print(f"Product: {result}")
            return result
        raise ValueError("Multiplier must be a positive number")

    def __str__(self) -> str:
        """
        Рядкове представлення об'єкта.
        """
        return f"Rectangle({self.width:.2f}, {self.height:.2f})"

# Тести
r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)

try:
    assert r1.get_square() == 8
    print("Test1 passed")
except AssertionError:
    print("Test1 failed")

try:
    assert r2.get_square() == 18
    print("Test2 passed")
except AssertionError:
    print("Test2 failed")

try:
    r3 = r1 + r2
    assert r3.get_square() == 26
    print("Test3 passed")
except AssertionError:
    print("Test3 failed")

try:
    r4 = r1 * 4
    assert r4.get_square() == 32
    print("Test4 passed")
except AssertionError:
    print("Test4 failed")

try:
    assert Rectangle(3, 6) == Rectangle(2, 9)
    print("Test5 passed")
except AssertionError:
    print("Test5 failed")
