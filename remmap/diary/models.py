from django.db import models
from datetime import datetime

class Diary(models.Model):
    
    class Meta:
        abstract = False
        
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    title = models.CharField(max_length=150,)
    content = models.TextField()
    date = models.DateField(default=datetime.now)
    def __str__(diary) -> str:
        return diary.title
    

class Music(models.Model):

    class Meta:
        abstract = False

    title = models.CharField(max_length=150)
    singer = models.CharField(max_length=150)

    def __str__(music) -> str:
        return music.title    