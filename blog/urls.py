from django.urls import path
from . import views
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns	 = [
	path('' , views.index , name = 'index'),
	path('business/' , views.business , name = 'business'),
	path('sports/' , views.sports , name = 'sports'),
	path('entertainment/' , views.entertainment , name = 'entertainment' ),
	path('register/' , user_views.register , name = 'register'),
	path('register/redirect/' , views.index , name = 'redirect'),
	path('login/' , auth_views.LoginView.as_view(template_name = 'users/login.html') , name = 'login'),
	path('logout/' , auth_views.LogoutView.as_view(template_name = 'users/logout.html') , name = 'logout'),
	path('profile/' , user_views.profile, name = 'profile'),
	path('business/business_post_add/' , views.business_post_add , name = 'business_post_add'),
	path('sports/sports_post_add/' , views.sports_post_add , name = 'sports_post_add'),
	path('entertainment/entertainment_post_add/' , views.entertainment_post_add , name = 'entertainment_post_add'),
	path('business/update_bussiness/<str:pk>/' , views.updatebussiness , name = 'updatebussiness'),
	path('business/delete_bussiness/<str:pk>/' , views.deletebussiness , name = 'deletebussiness'),
	path('sports/delete_sports/<str:pk>/' , views.deletesports , name = 'deletesports'),
	path('entertainment/delete_entertainment/<str:pk>/' , views.deleteentertainment , name = 'deleteentertainment'),
	path('sports/update_sports/<str:pk>/' , views.updatesports , name = 'updatesports'),
	path('entertainment/update_entertainment/<str:pk>/' , views.updateentertainment , name = 'updateentertainment'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL  , document_root = settings.MEDIA_ROOT)