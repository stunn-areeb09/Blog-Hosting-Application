from .form import UserRegisterForm
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
def register(request):
	if request.method == 'POST':
		if form.is_valid():
			form = UserRegisterForm(request.POST)	
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request , 'Account Created !')
			return redirect('login')
	else:
		form  = UserRegisterForm()
	return render(request , 'users/register.html' , {'form' : form}) 
# Create your views here.
@login_required
def profile(request):
	return render(request , 'users/profile.html')
