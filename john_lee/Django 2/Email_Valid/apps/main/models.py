from __future__ import unicode_literals
from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class EmailManager(models.Manager):
    def valid(self, email):
        criteria = []
        if len(email) < 1:
            criteria.append("Your email must be at least one character!")
        elif not EMAIL_REGEX.match(email):
            criteria.append("This email is not a valid email address!")

        if len(criteria) > 0:
            return (False, criteria)
        else:
            email = User.objects.create(email=email)
            email.save()
            return(True, email)

class User(models.Model):
    email = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = EmailManager()
