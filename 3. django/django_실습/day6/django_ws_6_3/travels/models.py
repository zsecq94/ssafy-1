from django.db import models

# Create your models here.

class Travel(models.Model):
    location = models.CharField(max_length=10) 
    plan = models.TextField()
    start_data = models.DateTimeField()
    end_data = models.DateTimeField()

    def __str__(self):
        return self.location