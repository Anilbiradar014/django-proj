from django.contrib import admin

# Register your models here.
from .models import Task, Review, Album, Song

admin.site.register(Task)
admin.site.register(Review)
admin.site.register(Album)
admin.site.register(Song)