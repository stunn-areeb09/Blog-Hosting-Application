from django.forms import ModelForm
from .models import E_Post


class update_entertainment(ModelForm):
	disabled_fields = ('author',)
	class Meta:
		model = E_Post
		fields = '__all__'

	def __init__(self, *args, **kwargs):
	    super(update_entertainment, self).__init__(*args, **kwargs)
	    for field in self.disabled_fields:
	    	self.fields[field].disabled = True