from django.db import models

# Create your models here.
class Login(models.Model):
    username=models.CharField(max_length=250)
    password=models.CharField(max_length=250)
    def __str__(self):
        return self.username + '-' + self.password
