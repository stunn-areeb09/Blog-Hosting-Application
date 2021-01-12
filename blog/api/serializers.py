from rest_framework import serializers

from blog.models import Post

class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = (
			'id',
			'url',
			'title',
			'content',
			'date_posted',
			'author',
		)