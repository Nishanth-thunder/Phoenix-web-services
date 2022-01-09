from django.db import models
class data(models.Model):
    name=models.CharField(max_length=200)
    role=models.CharField(max_length=300)
    age=models.CharField(max_length=10)
    location=models.CharField(max_length=100)
    experience=models.CharField(max_length=100)
    jobrole=models.CharField(max_length=200)
    class12=models.CharField(max_length=20)
    cgpa=models.CharField(max_length=10)
    email=models.CharField(max_length=30)


