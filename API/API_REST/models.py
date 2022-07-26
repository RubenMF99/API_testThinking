from django.db import models

class Company(models.Model):
    companyname=models.CharField(max_length=80)
    direction=models.CharField(max_length=40)
    NIT=models.PositiveIntegerField()
    cell=models.PositiveIntegerField()

