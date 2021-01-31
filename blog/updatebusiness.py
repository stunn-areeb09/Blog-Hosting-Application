from django.forms import ModelForm
from .models import Post 

class update_bussiness(ModelForm):
	class Meta:
		model  = Post
		fields = '__all__'
		