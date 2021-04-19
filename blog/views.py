from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Post, S_Post, E_Post
from django.contrib.auth.models import User
from django.contrib import messages
from .updatebusiness import update_bussiness
from .updatesports import update_sports
from .updateentertainment import update_entertainment
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
	messages.success( request , 'The blog with the  title %s is created successfully in the Bussiness Category !! ' %business_post_title)
	return render( request , 'blog/index.html' )

def sports_post_add(request):
	sports_post_content = request.POST["sports_post_blog"]
	sports_post_title = request.POST["sports_post_title"]
	if request.user.is_authenticated:
		sports_post_user = request.user
	sports = S_Post( title = sports_post_title , content = sports_post_content , author = sports_post_user )
	sports.save()
	messages.success( request , 'The blog with the  title %s is created successfully in the Sports Category !! ' %sports_post_title)
	return render ( request , 'blog/index.html' )

def entertainment_post_add(request):
	entertainment_post_content = request.POST["entertainment_post_content"]
	entertainment_post_title =  request.POST["entertainment_post_title"]
	if request.user.is_authenticated:
		entertainment_post_user = request.user
	entertianment = E_Post( title = entertainment_post_title, content = entertainment_post_content , author =  entertainment_post_user )
	entertianment.save()
	messages.success( request , 'The blog with the  title %s is created successfully in the Entertainment Category !! ' %entertainment_post_title)
	return render ( request ,  'blog/index.html' )

def updatebussiness( request , pk ):
	current_post = Post.objects.get( id = pk )
	form = update_bussiness(instance = current_post)
	updated_title = current_post.title
	if request.method == 'POST':
		#updated_title = request.POST["title"]
		form = update_bussiness(request.POST , instance = current_post)
		if form.is_valid():
			form.save()
			messages.success( request , 'The blog with the title {} is updated successfully in business Category by user {} !!'.format(updated_title , request.user))
			return redirect('/')
	context  = { 
		'form' : form 
	}
	return render ( request , 'blog/updatebussiness.html' , context ) 

def updatesports(request , pk ):
	current_post = S_Post.objects.get( id = pk )
	form = update_sports( instance = current_post)
	updated_title = current_post.title
	if request.method == 'POST':
		form = update_sports(request.POST , instance = current_post)
		if form.is_valid():
			form.save()
			messages.success( request , 'The blog with the title {} is updated successfully in Sports Category by user {} !!'.format(updated_title , request.user))
			return redirect('/')
	context = {
		'form' : form
	}
	return render (request , 'blog/updatesports.html' , context)

def updateentertainment(request , pk):
	current_post = E_Post.objects.get( id  = pk )
	form = update_entertainment( instance = current_post)
	updated_title = current_post.title
	if request.method == 'POST':
		form = update_sports(request.POST , instance = current_post)
		if form.is_valid():
			form.save()
			messages.success( request , 'The blog with the title {} is updated successfully in Entertianment Category by user {} !!'.format(updated_title , request.user))
			return redirect('/')
	context = {
		'form' : form
	}
	return render (request , 'blog/updateentertainment.html' , context )

def deletebussiness( request  , pk ):
	current_post = Post.objects.get( id = pk )
	if request.method == 'POST':
		deleted_title = current_post.title
		current_post.delete()
		messages.success( request , 'The blog with the title {} is deleted successfully in Business Category by user {} !!'.format(deleted_title , request.user) )
		return redirect('/')
	context = {
		'posts' : current_post
	}
	return render( request , 'blog/deletebussiness.html' , context )

def deletesports(request , pk):
	current_post = S_Post.objects.get(id = pk)
	if request.method == 'POST':
		deleted_title = current_post.title
		current_post.delete()
		messages.success( request , 'The blog with the title {} is deleted successfully in Sports Category by user {} !!'.format(deleted_title , request.user)  )
		return redirect('/')
	context = {
		'posts' : current_post
	}
	return render( request , 'blog/deletesports.html' , context )

def deleteentertainment( request , pk ):
	current_post = E_Post.objects.get( id = pk )
	if request.method == 'POST':
		deleted_title = current_post.title
		current_post.delete()
		messages.success( request , 'The blog with the title {} is deleted successfully in Entertianment Category by user {} !!'.format(deleted_title , request.user))
		return redirect('/')
	context = {
		'posts' : current_post
	}
	return render( request , 'blog/deleteentertainment.html' , context )