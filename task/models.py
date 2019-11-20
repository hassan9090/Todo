from django.db import models

# Create your models here.

class State(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

# add this
class Task(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.title