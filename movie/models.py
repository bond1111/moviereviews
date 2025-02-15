from django.db import models
#the import below will allow users post comments
from django.contrib.auth.models import User





class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='movie/images/')
    url = models.URLField(blank=True)

# Create your models here.
class Review(models.Model):
    text = models.CharField(max_length=100)
    date= models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    watchAgain = models.BooleanField()

    def __str__(self):
        return self.text