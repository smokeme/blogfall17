from rest_framework import serializers
from posts.models import Post

class PostListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = ['title', 'author', 'publish_date']

class PostDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = "__all__"