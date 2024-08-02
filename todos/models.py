from django.db import models
import uuid

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=255)
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False, primary_key=True)
    completed = False
    