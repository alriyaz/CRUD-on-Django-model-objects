# Django specific settings
import inspect
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.db import connection
# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from crud.models import *
from datetime import date


# Your code starts from here:
print("\n")

instructor_kr = Instructor.objects.get(first_name="Karishma")
print(instructor_kr)

print("\n")

try:
    instructor_andy = Instructor.objects.get(first_name="Andy")
except Instructor.DoesNotExist:
    print("2. Try to find a non-existing instructor with first name `Andy`")
    print("Instructor Andy doesn't exist")

print("\n")

full_time = Instructor.objects.exclude(full_time=False).filter(total_learners__gt=3000, first_name__startswith='Y')
print(full_time)

print("\n")