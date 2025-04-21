from django.db import models
from django.utils import timezone

# Create your models here.

class Todo(models.Model):
    text = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.text} - {'Done' if self.done else 'Pending'}"
