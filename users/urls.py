from django.urls import path
from . import views


app_name = 'users'

urlpatterns = [
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    
    path('password-change/', views.PasswordChangeUser.as_view(), name='password_change'),
    path('password-change/done/', views.PasswordChangeDoneUser.as_view(), name='password_change_done'),
    
    path('password-reset/', views.PasswordResetUser.as_view(), name='password_reset'),
    path('password-reset/done/', views.PasswordResetDoneUser.as_view(), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', views.PasswordResetConfirmUser.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', views.PasswordResetCompleteUser.as_view(), name='password_reset_complete'),
    
    path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile'),
    path('profile/<slug:slug>/', views.ProfileView.as_view(), name='profile'),
]