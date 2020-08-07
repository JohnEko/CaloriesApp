from django.db import models

# Create your models here.
class Sendemail(models.Model):
    email   = models.EmailField(max_length=30)
    subject = models.CharField(max_length=20, default=True)
    body    = models.TextField(default=True)

def __str__(self):
    return self.email