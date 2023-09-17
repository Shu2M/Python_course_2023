import random
from education_materials import EducationMaterials
from teacher import Teacher
from student import Student

MAX_NUM_STUDENT = 4

education_materials = EducationMaterials(
    'Python',
    'Version Control Systems',
    'Relational Databases',
    'NoSQL databases',
    'Message Brokers',
)

teacher = Teacher()
group_of_student = [Student() for _ in range(MAX_NUM_STUDENT)]

for course in education_materials.materials:
    students_on_course = random.sample(group_of_student, k=random.randrange(MAX_NUM_STUDENT))
    teacher.teach(course, students_on_course)

for student in group_of_student:
    print(student.knowledge)
    student.forget_knowledge()
    print(student.knowledge)
