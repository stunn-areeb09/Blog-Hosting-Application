from django.forms import ModelForm
from .models import Post 

class update_bussiness(ModelForm):
	disabled_fields = ('author',)
	class Meta:
		model  = Post
		fields = '__all__'

	def __init__(self , *args , **kwargs):
		super(update_bussiness , self).__init__(*args , **kwargs)
		for field in self.disabled_fields:
			self.fields[field].disabled = True
		