# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re
# Create your models here.
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
class UserManager(models.Manager):
    def validate(self, postData):
        errors=[]
        if len(postData['fName'])<1:
            errors.append("First name cannot be empty")
        else:
            if not NAME_REGEX.match(postData['fName']):
                errors.append("Invalid first name")
        if len(postData['lName'])<1:
            errors.append("Last name cannot be empty")
        else:
            if not NAME_REGEX.match(postData['lName']):
                errors.append("Invalid last name")
        if len(postData['email'])<1:
            errors.append("Email cannot be empty")
        else:
            if not EMAIL_REGEX.match(postData['email']):
                errors.append("Invalid email")
        return errors
            
        

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    objects = UserManager()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)