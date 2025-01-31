class Human:
    """
    Клас, що представляє людину.
    """

    def __init__(self, gender: str, age: int, first_name: str, last_name: str):
        """
        Ініціалізує об'єкт людини.
        """
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        """
        Повертає рядкове представлення людини.
        """
        return f"{self.first_name} {self.last_name}, {self.age} years old, {self.gender}"


class Student(Human):
    """
    Клас, що представляє студента (наслідує Human).
    """

    def __init__(self, gender: str, age: int, first_name: str, last_name: str, record_book: str):
        """
        Ініціалізує об'єкт студента.
        """
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self) -> str:
        """
        Повертає рядкове представлення студента.
        """
        return f"{super().__str__()}, Record Book: {self.record_book}"


class GroupLimitException(Exception):
    """
    Користувацьке виключення для перевищення ліміту студентів у групі.
    """
    pass


class Group:
    """
    Клас, що представляє групу студентів.
    """
    max_students = 10

    def __init__(self, number: str):
        """
        Ініціалізує групу студентів.
        """
        self.number = number
        self.group: list[Student] = []

    def add_student(self, student: Student) -> None:
        """
        Додає студента до групи.
        """
        if len(self.group) >= self.max_students:
            raise GroupLimitException(f"Cannot add student {student.first_name} {student.last_name}. The group is full!")
        if student in self.group:
            print(f"Student {student.first_name} {student.last_name} is already in the group.")
            return
        self.group.append(student)

    def find_student(self, last_name: str) -> None:
        """
        Шукає студента за прізвищем.
        """
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name: str) -> None:
        """
        Видаляє студента за прізвищем.
        """
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)
            print(f"Student {last_name} has been removed.")
        else:
            print(f"No student with last name {last_name} found.")

    def __str__(self) -> str:
        """
        Повертає рядкове представлення групи.
        """
        all_students = '\n'.join(str(student) for student in self.group)
        return f"Group: {self.number}\n{all_students}"


# Створення студентів
st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
students = [Student('Male', 20 + i, f'Name{i}', f'Surname{i}', f'ID{i}') for i in range(9)]

# Створення групи
gr = Group('PD1')
try:
    for student in students:
        gr.add_student(student)
    gr.add_student(st1)
    gr.add_student(st2)
except GroupLimitException as e:
    print(f"Error: {e}")

# Вивід інформації про групу
print(gr)
