from rest_framework import serializers
from .models import Post, Comment

# Create your views here.

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','content', 'timestamp', 'view_count']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['post_id', 'content', 'timestamp']