from rest_framework import serializers
from .models import Post, Comment

# Create your views here.

class PostSerializer(serializers.ModelSerializer):

    comment_count = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ['id','content', 'timestamp', 'view_count', 'comment_count']

    def get_comment_count(self, obj):
        return obj.comment_set.count()


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['post_id', 'content', 'timestamp']