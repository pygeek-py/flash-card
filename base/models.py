from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=800)
    answer = models.CharField(max_length=800)