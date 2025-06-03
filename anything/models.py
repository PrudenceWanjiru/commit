from django.db import models

# Create your models here.
class Students(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    sports = models.CharField(max_length=100,null=True,blank=True)
    education = models.CharField(max_length=30)
    class Meta:
        db_table = 'students'
        #python manage.py makemigrations
        #python manage.py migrate
        #pip install django_rest_framework