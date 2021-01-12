from django.urls import path
from . import views
from blog import views as blog_views
urlpatterns = [
	path(''  , blog_views.index , name = 'blog_index'),
]