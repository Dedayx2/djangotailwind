from email.policy import default
import re
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    # id
    title = models.CharField(max_length=500)
    describtion = models.TextField()
    date = models.DateField()
    done = models.BooleanField(default=False)


    def __str__(self):
        return self.title 
    
    def get_absolute_url(self):
        return reverse('home')
