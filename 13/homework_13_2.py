class Counter:
    """
    Клас цифрового лічильника.
    Дозволяє встановлювати мінімальне, максимальне та початкове значення.
    Лічильник може збільшуватись (step_up) та зменшуватись (step_down) у межах визначеного діапазону.
    """

    def __init__(self, current: int = 1, min_value: int = 0, max_value: int = 10) -> None:
        """
        Ініціалізація лічильника.
        """
        self.min_value = min_value
        self.max_value = max_value

        if not (min_value <= current <= max_value):
            raise ValueError("Initial value is out of range")

        self.current = current

    def set_current(self, start: int) -> None:
        """
        Встановлює поточне значення лічильника.
        """
        if not (self.min_value <= start <= self.max_value):
            raise ValueError("Value is out of allowed range")
        self.current = start

    def set_max(self, max_value: int) -> None:
        """
        Встановлює максимальне значення лічильника.
        """
        if max_value < self.min_value:
            raise ValueError("Maximum value cannot be less than minimum value")
        self.max_value = max_value
        if self.current > self.max_value:
            self.current = self.max_value

    def set_min(self, min_value: int) -> None:
        """
        Встановлює мінімальне значення лічильника.
        """
        if min_value > self.max_value:
            raise ValueError("Minimum value cannot be greater than maximum value")
        self.min_value = min_value
        if self.current < self.min_value:
            self.current = self.min_value

    def step_up(self) -> None:
        """
        Збільшує значення лічильника на 1.
        """
        if self.current >= self.max_value:
            raise ValueError("Maximum limit reached")
        self.current += 1

    def step_down(self) -> None:
        """
        Зменшує значення лічильника на 1.
        """
        if self.current <= self.min_value:
            raise ValueError("Minimum limit reached")
        self.current -= 1

    def get_current(self) -> int:
        """
        Повертає поточне значення лічильника.
        """
        return self.current


# Перевірка роботи класу
counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
assert counter.get_current() == 10, 'Test1'
try:
    counter.step_up()
except ValueError as e:
    print(e)
assert counter.get_current() == 10, 'Test2'

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
assert counter.get_current() == 7, 'Test3'
try:
    counter.step_down()
except ValueError as e:
    print(e)
assert counter.get_current() == 7, 'Test4'
