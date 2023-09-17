from student import Student
from human import Human


class Teacher(Human):
    def __init__(
            self,
            num_graduated_students: int = 0,
            *args,
            **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.num_graduated_students = num_graduated_students

    def teach(self, education_material: str, students: list[Student]):
        for student in students:
            student.take(education_material)
            self.num_graduated_students += 1
