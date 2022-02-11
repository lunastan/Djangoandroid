from rest_framework import serializers
from rest_framework.serializers import (ModelSerializer)
from .models import Post


class CreateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['user', 'model_pic', 'lat', 'lng']
