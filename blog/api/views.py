from django.shortcuts import render 
from rest_framework import viewsets
from blog.models import Post
from .serializers import PostSerializer
class BlogRudView(viewsets.ModelViewSet):
	"""docstring for BlogRudView"""
	queryset = Post.objects.all()
	serializer_class = PostSerializer

