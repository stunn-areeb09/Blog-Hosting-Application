from django.forms import ModelForm
from .models  import S_Post

class update_sports(ModelForm):
	disabled_fields = ('author',)
	class Meta:
		model = S_Post
		fields = '__all__'

	def __init__(self , *args , **kwargs):
		super(update_sports , self).__init__(*args, **kwargs)
		for field in self.disabled_fields:
			self.fields[field].disabled = True
		    
