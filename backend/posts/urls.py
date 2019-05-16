""" route definitions for posts app """
from django.urls import path

from .views import PostList, PostDetail

urlpatterns = [
    path('<int:pk>/', PostDetail.as_view()),
    path('', PostList.as_view())
]
