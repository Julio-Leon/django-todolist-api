from django.db import models
from rest_framework import serializers
from .models import ToDo

class ToDoSerializer(serializers.HyperlinkedModelSerializer):
    todo_url = serializers.ModelSerializer.serializer_url_field('todos_detail')
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = ToDo
        fields = ('id', 'title', 'todo_url', 'owner')