from django.db import models
from django.conf import settings

class Todo(models.Model):
    title = models.CharField(max_length=50)
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )