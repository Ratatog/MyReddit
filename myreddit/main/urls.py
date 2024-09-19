from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('search/tags/<tag>/', views.TagHome.as_view(), name='search_tags'),
    
    path('post/<int:pk>/', views.ShowPost.as_view(), name='post'),
    path('post/create/', views.CreatePost.as_view(), name='add_post'),
    
    path('group/<int:pk>/', views.GroupView.as_view(), name='group'),
    path('group/create/', views.GroupCreateView.as_view(), name='group'),
    
    
    path('like_post/<int:pk>/', views.LikePostView, name='like_post'),
    path('like_comm/<int:pk>/', views.LikeCommView, name='like_comm'),
]
