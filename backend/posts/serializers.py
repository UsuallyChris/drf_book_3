""" serializers for posts app """
from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    """ serializer for Post model """
    class Meta:
        fields = ('id', 'author', 'title', 'body', 'created_at', )
        model = Post
