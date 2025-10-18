from django.db import models
from models.users.models import User

class Quiz(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )

    time = models.IntegerField()
    memory = models.IntegerField()
    difficulty_level = models.IntegerField()

    name = models.CharField(max_length=255,null=True)

    description = models.TextField(null=True)
    input_desc = models.TextField()
    output_desc = models.TextField()

