class Item:

    def __init__(self, name: str, price: int, description: str, dimensions: str):
        """
        Ініціалізація товару.
        """
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self) -> str:
        """
        Повертає рядок, який містить назву та ціну товару.
        """
        return f"{self.name}, price: {self.price}"


class User:

    def __init__(self, name: str, surname: str, numberphone: str):
        """
        Ініціалізація користувача.
        """
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self) -> str:
        """
        Повертає рядок, який містить ім'я та прізвище користувача.
        """
        return f"{self.name} {self.surname}"


class Purchase:

    def __init__(self, user: User):
        """
        Ініціалізація покупки.
        """
        self.user = user
        self.products = {}

    def add_item(self, item: Item, cnt: int) -> None:
        """
        Додає товар до кошика, замінюючи кількість товару.
        """
        if cnt <= 0:
            return
        # Заміна кількості товару на нову
        self.products[item] = cnt

    def get_total(self) -> int:
        """
        Повертає загальну суму покупки.
        """
        return sum(item.price * quantity for item, quantity in self.products.items())

    def __str__(self) -> str:
        """
        Повертає опис покупки у вигляді рядка.
        """
        items_str = "\n".join(f"{item.name}: {quantity} pcs." for item, quantity in self.products.items())
        return f"User: {self.user}\nItems:\n{items_str}"


# Створення товарів
lemon = Item('lemon', 5, "yellow", "small")
apple = Item('apple', 2, "red", "middle")

# Створення покупця
buyer = User("Ivan", "Ivanov", "02628162")

# Створення покупки
cart = Purchase(buyer)

# Додаємо перші товари до кошика
cart.add_item(lemon, 4)  # Додаємо 4 лимони
cart.add_item(apple, 20)  # Додаємо 20 яблук

print("Початковий кошик:")
print(cart)


# Функція для виконання перевірок
def test_assertions() -> None:
    """
    Виконує перевірки за допомогою assert, щоб перевірити правильність роботи функцій.
    """
    try:
        # Перевірка, що користувач є екземпляром класу User
        assert isinstance(cart.user, User), "User should be an instance of the User class"
        print("Assertion 1 passed: User is an instance of the User class.")

        # Перевірка, що загальна сума покупки дорівнює 60
        assert cart.get_total() == 60, "Total should be 60"
        print("Assertion 2 passed: Total is 60.")

        # Перевірка, що загальна сума покупки залишилась 60 після попередньої перевірки
        assert cart.get_total() == 60, "Total should remain 60"
        print("Assertion 3 passed: Total remains 60.")

        # Заміна кількості яблук на нову (10 замість 20)
        cart.add_item(apple, 10)  # Заміна кількості яблук на 10
        print("Кошик після зміни кількості яблук:")
        print(cart)  # Виведення кошика після зміни кількості

        # Перевірка, що тепер сума повинна бути 40
        assert cart.get_total() == 40, "Total should be 40 after changing apple quantity"
        print("Assertion 4 passed: Total is 40 after changing apple quantity.")

    except AssertionError as e:
        print(f"Assertion failed: {e}")


# Виконання перевірок
test_assertions()
