from django.contrib import admin
from .models import Post, S_Post  , E_Post
# Register your models here.
admin.site.register(Post)
admin.site.register(S_Post)
admin.site.register(E_Post)