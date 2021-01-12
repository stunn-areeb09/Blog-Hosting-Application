from .views import BlogRudView
from django.contrib import admin
from django.urls import path , include

from rest_framework import routers

router = routers.DefaultRouter()
router.register( ''  , BlogRudView )
urlpatterns = [
    path('', include(router.urls) )
]