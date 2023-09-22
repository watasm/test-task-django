import os
import django

# Установите переменную окружения DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

# Инициализируйте Django
django.setup()


import random
from faker import Faker
from django.utils import timezone

from movies.models import Movie


fake = Faker()


for i in range(10):
    description = fake.paragraph()

for i in range(20):
    title = fake.sentence()
    description = fake.paragraph()
    release_date = fake.date_between(start_date='-30y', end_date='today')
    price = round(random.uniform(1, 100), 2)
    mda = fake.lexify(text='???')
    movie = Movie.objects.create(title=title, mda=mda, description=description, release_date=release_date, price=price)
    movie.save()
