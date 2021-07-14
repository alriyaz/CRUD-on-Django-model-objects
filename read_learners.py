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
learners = Learner.objects.filter(last_name="Smith")
print(learners)

print("\n")

young= Learner.objects.order_by('-dob')[0:2]
print(young)