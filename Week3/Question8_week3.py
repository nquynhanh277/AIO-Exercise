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


class Ward:
    def __init__(self, name: str):
        self.__name = name
        self.__listPeople = list()

    def add_person(self, person: Person):
        self.__listPeople.append(person)

    def describe(self):
        print(f"Ward name: {self_name}")
        for p in self.__listPeople:
            p.describe()

    def count_doctor(self):
        number = 0
        for p in self.__listPeople:
            if isinstance(p, Doctor):  # if p's type is doctor
                number = number + 1
        return number


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
    student1 = Student(name="studentA", yob=2010, grade="7")
    teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
    teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
    doctor1 = Doctor(name="doctorA", yob=1945,
                     specialist="Endorcrinologists")
    doctor2 = Doctor(name="doctorB", yob=1975,
                     specialist="Cardiologists")

    ward1 = Ward(name="Ward1")
    ward1.add_person(student1)
    ward1.add_person(teacher1)
    ward1.add_person(teacher2)
    ward1.add_person(doctor1)
    ward1.add_person(doctor2)
    print(ward1.count_doctor())
