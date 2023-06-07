from django.db import models

# Create your models here.
class Task(models.Model):

    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)

class Review(models.Model):

    reviewer_name = models.CharField(max_length=100)
    review_title = models.CharField(max_length=100)

    task = models.ForeignKey(Task, on_delete=models.CASCADE)

class Album(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    def __str__(self):
        return self.title
  
class Song(models.Model):
    name = models.CharField(max_length=50)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
