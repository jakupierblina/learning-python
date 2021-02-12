from django.db import models

# Create your models here.

#user's class



#class todo
class Todo(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

