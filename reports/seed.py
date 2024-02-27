from faker import Faker
from .models import *
import random
from django.db.models import Sum

fake = Faker()

def seed_db(n=10) -> None:
    try:
        for _ in range(n):
            departments_objs = Department.objects.all()
            random_index = random.randint(0, len(departments_objs)-1)
            department = departments_objs[random_index]
            student_id = f'22CS{random.randint(3000, 4000)}'
            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(18,25)
            student_address = fake.address()

            student_id_obj = StudentID.objects.create(student_id = student_id)

            student_obj = Student.objects.create(
                department = department,
                student_id = student_id_obj,
                student_name = student_name,
                student_email = student_email,
                student_age = student_age,
                student_address = student_address,
            )

    except Exception as e:
        print(e)


def generate_report_card():
    current_rank = -1
    ranks = Student.objects.annotate(marks = Sum('studentmarks__marks')).order_by('-marks', 'student_age')

    i = 1
    for rank in ranks:
        ReportCard.objects.create(
            student = rank,
            student_rank = i
        )
        i=i+1