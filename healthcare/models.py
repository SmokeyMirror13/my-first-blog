from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Patients(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=250) 
    age = models.CharField(max_length=3)
    medical_info = {}
    medical_info['hr'] = []
    medical_info['tmp'] = []
    medical_info['time'] = []
    medical_info['condition'] = []
    def append(self, heartrate, temperature, c):
        self.medical_info['hr'].append(hr)
        self.medical_info['tmp'].append(temperature)
        self.medical_info['time'].append(timezone.localtime())
        self.medical_info['condition'].append(c)