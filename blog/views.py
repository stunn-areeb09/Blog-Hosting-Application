from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def index(request):
	return render( request , 'blog/index.html' )
	
def business(request):
	context  =
	{
		'posts' : Post.objects.all()
	}
	return render( request , 'blog/business.html' , context)

def entertainment(request):
	context = 
	{
		'posts' : E_Post.objects.all()
	}
	return render( request , 'blog/entertainment.html' , context )

def sports(request):
	context 
	{
		'posts' : S_Post.objects.all()
	}
	return render( request  , 'blog/sports.html' , context)
