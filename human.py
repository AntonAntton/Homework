class Human:
    """
    Клас, що описує людину
    """
    def __init__(self, gender: str, age: int, first_name: str, last_name: str):
        """
        Конструктор класу Human
        """
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        """
        Метод повертає інформацію про людину у вигляді рядка
        """
        return f"{self.first_name} {self.last_name}, {self.age} years old, {self.gender}"
