from student import Student


class Teacher:
    def __init__(self, num_graduated_students: int = 0):
        self.num_graduated_students = num_graduated_students

    def teach(self, education_material: str, students: list[Student]):
        for student in students:
            student.take(education_material)
            self.num_graduated_students += 1
