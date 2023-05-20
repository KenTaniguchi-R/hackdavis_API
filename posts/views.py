
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Post, Comment
from .serializer import CommentSerializer, PostSerializer

class PostView(APIView):
    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        posts = Post.objects.all().order_by('-timestamp')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Save a post.
        """
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class CommentList(APIView):
    def get(self, request, format=None):
        """
        Return a list of comment for a post.
        """
        post_id = request.GET.get('post_id')
        comments = Comment.objects.filter(post_id=post_id).order_by('-timestamp')
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Save a comment for a post.
        """
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)