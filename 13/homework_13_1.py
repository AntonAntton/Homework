class Human:
    """
    Базовий клас, що представляє людину.
    """

    def __init__(self, gender: str, age: int, first_name: str, last_name: str) -> None:
        """
        Ініціалізація об'єкта класу Human.
        """
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        """
        Повертає рядкове представлення об'єкта.
        """
        return f"{self.first_name} {self.last_name}, {self.age} years old, {self.gender}"


class Student(Human):
    """
    Клас, що представляє студента (наслідує клас Human).
    """

    def __init__(self, gender: str, age: int, first_name: str, last_name: str, record_book: str) -> None:
        """
        Ініціалізація об'єкта класу Student.
        """
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self) -> str:
        """
        Повертає рядкове представлення студента.
        """
        return f"{super().__str__()}, Record Book: {self.record_book}"


class Group:
    """
    Клас, що представляє групу студентів.
    """

    def __init__(self, number: str) -> None:
        """
        Ініціалізація об'єкта класу Group.
        """
        self.number = number
        self.group: set[Student] = set()

    def add_student(self, student: Student) -> None:
        """
        Додає студента до групи.
        """
        self.group.add(student)

    def find_student(self, last_name: str) -> None:
        """
        Пошук студента за прізвищем.
        """
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name: str) -> None:
        """
        Видаляє студента з групи за прізвищем.
        """
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def __str__(self) -> str:
        """
        Повертає рядкове представлення групи та її студентів.
        """
        all_students = '\n'.join(str(student) for student in self.group)
        return f"Group: {self.number}\n{all_students}"


# Приклад використання
st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')

gr.add_student(st1)
gr.add_student(st2)
print(gr)

assert str(gr.find_student('Jobs')) == str(st1), f"Test1 Failed: Expected {str(st1)}"
assert gr.find_student('Jobs2') is None, f"Test2 Failed: Expected None"
assert isinstance(gr.find_student('Jobs'), Student), f"Test3 Failed: Expect instance of Student"

print(str(gr.find_student('Jobs')))
print(gr.find_student('Jobs2'))
print(isinstance(gr.find_student('Jobs'), Student))

gr.delete_student('Taylor')
print(gr)

gr.delete_student('Taylor')
