from django.db import models


class Enquiry (models.Model):# datatype access--Model
   
    name=models.CharField(max_length=15)
    email=models.CharField(max_length=10)
    phone=models.CharField(max_length=10)
