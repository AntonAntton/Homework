from human import Human

class Student(Human):
    """
    Клас, що описує студента, є підкласом Human
    """
    def __init__(self, gender: str, age: int, first_name: str, last_name: str, record_book: str):
        """
        Конструктор класу Student
        """
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self) -> str:
        """
        Метод повертає інформацію про студента у вигляді рядка
        """
        return f"{super().__str__()}, Record book: {self.record_book}"

    def __eq__(self, other: object) -> bool:
        """
        Метод для порівняння студентів
        """
        return isinstance(other, Student) and str(self) == str(other)

    def __hash__(self) -> int:
        """
        Метод повертає хеш-код об'єкта студента
        """
        return hash(str(self))
