import random
from education_materials import EducationMaterials
from teacher import Teacher
from student import Student


education_materials = EducationMaterials(
    'Python',
    'Version Control Systems',
    'Relational Databases',
    'NoSQL databases',
    'Message Brokers',
)

teacher = Teacher()
group_of_student = [Student() for _ in range(4)]

for course in education_materials.materials:
    num_students_on_course = random.randrange(4)
    teacher.teach(course, random.sample(group_of_student, k=num_students_on_course))

for student in group_of_student:
    print(student.knowledge)

