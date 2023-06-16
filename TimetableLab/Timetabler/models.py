from tkinter import CASCADE
from django.db import models
from django_random_id_model import RandomIDModel
from django.contrib.auth.models import AbstractUser
import uuid
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class Teacher(RandomIDModel):
    name = models.CharField(max_length=50)
    totalHours = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Availability(models.Model):
    period = models.CharField(max_length=20)
    week = models.IntegerField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

class Module(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    week = models.IntegerField()
    year = models.IntegerField()
    period = models.CharField(max_length=20)

class Constraint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    required = models.BooleanField()