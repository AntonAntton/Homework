from student import Student


class GroupLimitException(Exception):
    """
    Користувацький виняток для перевищення ліміту студентів у групі
    """
    pass


class Group:
    """
    Клас, що описує групу студентів
    """
    max_students = 10

    def __init__(self, number: str):
        """
        Конструктор класу Group
        """
        self.number = number
        self.group: set[Student] = set()

    def add_student(self, student: Student) -> None:
        """
        Метод додає студента до групи
        """
        if len(self.group) >= self.max_students:
            raise GroupLimitException(f"Cannot add student {student.first_name} {student.last_name}. The group is full!")
        self.group.add(student)

    def find_student(self, last_name: str) -> None:
        """
        Метод шукає студента за прізвищем
        """
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name: str) -> None:
        """
        Метод видаляє студента за прізвищем
        """
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def __str__(self) -> str:
        """
        Метод повертає список студентів групи у вигляді рядка
        """
        all_students = '\n'.join(str(student) for student in self.group)
        return f"Group: {self.number}\n{all_students}"