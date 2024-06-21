from abc import ABC, abstractclassmethod


class Person(ABC):
    def __init__(self, name: str, yob: int):
        self._name = name
        self._yob = yob

    def get_yob(self):
        return self._yob

    @abstractclassmethod
    def describe(self):
        pass


class Student(Person):
    def __init__(self, name: str, yob: int, grade: str):
        super().__init__(name=name, yob=yob)
        self._grade = grade

    def describe(self):
        print(
            f"Student - Name: {self._name} - YoB: {self._yob} - Grade: {self._grade}")


class Teacher(Person):
    def __init__(self, name: str, yob: int, subject: str):
        super().__init__(name=name, yob=yob)
        self._subject = subject

    def describe(self):
        print(
            f"Teacher - Name: {self._name} - YoB: {self._yob} - Subject: {self._subject}")


class Doctor(Person):
    def __init__(self, name: str, yob: int, specialist: str):
        super().__init__(name=name, yob=yob)
        self._specialist = specialist

    def describe(self):
        print(
            f"Doctor - Name: {self._name} - YoB: {self._yob} - Speccialist: {self._specialist}")


if __name__ == "__main__":
    student1 = Student(name="StudentZ2023", yob=2011, grade="6")
    teacher1 = Teacher(name="TeacherZ2023", yob=1991, subject="History")
    doctor1 = Doctor(name="DoctorZ2023", yob=1981,
                     specialist="Endorcrinologists")
    assert student1._yob == 2011
    assert teacher1._yob == 1991
    assert doctor1._yob == 1981
    student1.describe()
    teacher1.describe()
    doctor1.describe()
