from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.PostView.as_view()),
    path('comment/', views.CommentList.as_view()),
]
