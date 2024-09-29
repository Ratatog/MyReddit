from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('subscriptions/', views.SubscriptionsView.as_view(), name='subscriptions'),
    path('all/', views.AllHomeView.as_view(), name='all_home'),
    
    path('search/', views.Search.as_view(), name='search'),
    path('search/tags/<slug:tag>/', views.SearchTagView.as_view(), name='search_tags'),
    path('search/post_title/<str:title>/', views.SearchPostTitleView.as_view(), name='search_post_title'),
    path('search/group_title/<str:title>/', views.SearchGroupTitleView.as_view(), name='search_group_title'),
    path('search/username/<slug:username>/', views.SearchUsernameView.as_view(), name='search_username'),
    
    path('post/<int:pk>/', views.ShowPost.as_view(), name='post'),
    path('post/create/', views.CreatePost.as_view(), name='add_post'),
    
    path('group/<int:pk>/', views.GroupView.as_view(), name='group'),
    path('group/create/', views.GroupCreateView.as_view(), name='create_group'),
    
    path('like_post/<int:pk>/', views.LikePostView, name='like_post'),
    path('like_comm/<int:pk>/', views.LikeCommView, name='like_comm'),
    
    path('group/join/<int:pk>/', views.JoinGroupView, name='join_group'),
    path('group/quit/<int:pk>/', views.QuitGroupView, name='quit_group'),
]
