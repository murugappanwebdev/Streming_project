from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
class Movies(models.Model):
    GENRES = (
        (1, "Imaginative Adventures"),
        (2, "New to Stremia"),
        (3, "Action Movies"),
        (4, "Us action & Adventure Movies"),
        (5, "Us movie dubbed in Tamil"),
        (6, "Blockbuster Us Comidies"),     
    )
    title = models.CharField(max_length=100)
    cast =  models.CharField(max_length=100)
    genre=models.IntegerField(choices=GENRES)
    description = models.TextField(max_length=500)
    cover_image = models.ImageField(upload_to='media/')
    video = models.FileField(upload_to='media/videos/')
    def _str_(self):
        return self.title
    # tv database
class Home(models.Model):
      GENRES = (
        (1, "Tv show dubbed in Tamil"),
        (2, "Violent movies"),
        (3, "Only on Streamia"),
        (4, "Sci-Fi Films"),
        (5, "Crime action"),
        (6, "Epics"),     
    )
      title = models.CharField(max_length=100)
      cast= models.CharField(max_length=100)
      genre=models.IntegerField(choices=GENRES)
      description = models.TextField(max_length=500)
      cover_image = models.ImageField(upload_to='media/')
      video = models.FileField(upload_to='media/videos/')
      def _str_(self):
        return self.title
class payment(models.Model):
      GENRES = (
        (1, "Tv show dubbed in Tamil"),
        (2, "Violent movies"),
        (3, "Only on Streamia"),
        (4, "Sci-Fi Films"),
        (5, "Crime action"),
        (6, "Epics"),     
    )
      title = models.CharField(max_length=100)
      cast= models.CharField(max_length=100)
      genre=models.IntegerField(choices=GENRES)
      description = models.TextField(max_length=500)
      cover_image = models.ImageField(upload_to='media/')
      def _str_(self):
        return self.title      