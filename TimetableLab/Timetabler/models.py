from django.db import models
from django_random_id_model import RandomIDModel
from django.contrib.auth.models import AbstractUser
import uuid


#class User(AbstractUser):
#    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class Teacher(RandomIDModel):
    name = models.CharField(max_length=50)

class Availability(models.Model):
    start = models.IntegerField()
    end = models.IntegerField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)