from django.db import models

# Create your models here.
class Task(models.Model):
     title=models.CharField(max_length=300)
     complete=models.BooleanField(default=False)
     created=models.DateTimeField(auto_now_add=True)
     objects = models.Manager()
     def __str__(self):
         return self.title
    
