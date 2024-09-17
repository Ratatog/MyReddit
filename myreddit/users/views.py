from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth import logout
from .forms import  RegisterUserForm, LoginUserForm, PasswordChangeUserForm, PasswordResetUserForm, \
    PasswordResetConfirmUserForm

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')
    extra_context = {'title': 'Register'}

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('home')
    extra_context = {'title': 'Login'}
    
class PasswordChangeUser(PasswordChangeView):
    form_class = PasswordChangeUserForm
    template_name = 'users/password_change.html'
    success_url = reverse_lazy('users:password_change_done')
    extra_context = {'title': 'Change Password'}

class PasswordChangeDoneUser(PasswordChangeDoneView):
    template_name = 'users/password_change_done.html'
    extra_context = {'title': 'Congratulations'}

class PasswordResetUser(PasswordResetView):
    form_class = PasswordResetUserForm
    template_name='users/password_reset_form.html'
    email_template_name="users/password_reset_email.html"
    success_url=reverse_lazy('users:password_reset_done')
    extra_context = {'title': 'Reset Password By Email'}
    
class PasswordResetDoneUser(PasswordResetDoneView):
    template_name='users/password_reset_done.html'
    extra_context = {'title': 'Reset Password'}

class PasswordResetConfirmUser(PasswordResetConfirmView):
    form_class = PasswordResetConfirmUserForm
    template_name='users/password_reset_confirm.html'
    success_url=reverse_lazy('users:password_reset_complete')
    extra_context = {'title': 'Reset Password'}

class PasswordResetCompleteUser(PasswordResetCompleteView):
    template_name='users/password_reset_complete.html'
    extra_context = {'title': 'Congratulations'}