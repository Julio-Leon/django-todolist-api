from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class ToDo(models.Model):
    owner = models.ForeignKey('todo_list.User', related_name='todos', on_delete=CASCADE)
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

def __str__(self):
        return self.title