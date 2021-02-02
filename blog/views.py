from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Post, S_Post, E_Post
from django.contrib.auth.models import User
from django.contrib import messages
from .updatebusiness import update_bussiness

def index(request):
	return render( request , 'blog/index.html' )
	
def business(request):
	context  ={
		'posts' : Post.objects.all()
	}
	return render( request , 'blog/business.html' , context)

def entertainment(request):
	context = {
		'posts' : E_Post.objects.all()
	}
	return render( request , 'blog/entertainment.html' , context )

def sports(request):
	context =  {
		'posts' : S_Post.objects.all()
	}
	return render( request  , 'blog/sports.html' , context)

def business_post_add(request):
	business_post_content = request.POST["business_post_content"]
	business_post_title = request.POST["business_post_title"]
	if request.user.is_authenticated:
		business_post_user = request.user
	business = Post( title = business_post_title , content = business_post_content  , author = business_post_user )
	business.save()
	messages.success( request , 'The blog with the  title %s is created successfully !! ' %business_post_title)
	return render( request , 'blog/index.html' )

def sports_post_add(request):
	sports_post_content = request.POST["sports_post_content"]
	sports_post_title = request.POST["sports_post_title"]
	if request.user.is_authenticated:
		sports_post_user = request.user
	sports = S_Post( title = sports_post_title , content = sports_post_content , author = sports_post_user )
	sports.save()
	messages.success( request , 'The blog with the  title %s is created successfully !! ' %sports_post_title)
	return render ( request , 'blog/index.html' )

def entertainment_post_add(request):
	entertainment_post_content = request.POST["entertainment_post_content"]
	entertainment_post_title =  request.POST["entertainment_post_title"]
	if request.user.is_authenticated:
		entertainment_post_user = request.user
	entertianment = E_Post( title = entertainment_post_title, content = entertainment_post_content , author =  entertainment_post_user )
	entertianment.save()
	messages.success( request , 'The blog with the  title %s is created successfully !! ' %entertainment_post_title)
	return render ( request ,  'blog/index.html' )

def updatebussiness(request):
	form = update_bussiness()
	if request.method == 'POST':
		print( 'printing post' , request.POST)
		updated_title = request.POST["title"]
		form = update_bussiness(request.POST)
		if form.is_valid():
			form.save()
			messages.success( request , 'The blog with the title %s is updated successfully !!' %updated_title)
			return redirect('/')
	context  = { 
		'form' : form 
	}
	return render ( request , 'blog/updatebussiness.html' , context ) 