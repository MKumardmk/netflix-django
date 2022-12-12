from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
AGE_CHOICES=(
    ('All','All'),
    ('kids','kids')
)
MOVIE_CHOICES=(
    ('sesanol','Seasonal'),
    ('single','Single')
)
# Create your models here.
class CustomUser(AbstractUser):
    profiles= models.ManyToManyField('profile',blank=True)
  
  
class Profile(models.Model):
    name= models.CharField( max_length=50) 
    # email=  models.EmailField( max_length=254) 
    age =models.CharField(max_length=5,default='ALL')
    uuid= models.UUIDField(default=uuid.uuid4)

class Movie(models.Model):
    title= models.CharField(max_length=100)
    description= models.TextField(max_length=250, blank=True, null=True)
    created= models.DateTimeField(auto_now_add=True)
    uuid= models.UUIDField(default=uuid.uuid4)
    types= models.CharField(max_length=10,choices=MOVIE_CHOICES)
    video= models.ManyToManyField('video')
    flyer= models.ImageField(upload_to='flyers')
    age_limit= models.CharField(max_length=5,choices=AGE_CHOICES)
    
class Video(models.Model):
     title= models.CharField(max_length=225,blank=True,null=True)
     file= models.FileField(upload_to='movies')
     #30 mins
     #pip freeze > requirements.txt 