#models.py
from django.db import models

class user(models.Model):
    name=models.CharField(max_length=20)
    passwd=models.CharField(max_length=20)
    username=models.CharField(max_length=30)
