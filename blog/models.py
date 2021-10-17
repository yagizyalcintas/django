from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title= models.CharField(max_length = 100)
    content = models.TextField()
    date = models.DateTimeField(auto_now = True)
    auth = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title