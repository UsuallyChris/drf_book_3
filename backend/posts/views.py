""" view class definitions for posts app """
from rest_framework import generics

from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    """ Post collection API endpoint """
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Singe Post endpoint """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
