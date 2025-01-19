from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, CreateView, UpdateView
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth import logout, get_user_model
from .forms import  RegisterUserForm, LoginUserForm, PasswordChangeUserForm, PasswordResetUserForm, PasswordResetConfirmUserForm, UpdateUserForm
from main.models import Notification
from main.utils import LoginMixn

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))

def friend(request, method, u1, u2):
    u1 = get_user_model().objects.get(username=u1)
    u2 = get_user_model().objects.get(username=u2)
    
    html1 = f"<a class='text-success' href='{reverse_lazy('users:profile', args=(u1.pk,))}'>{u1}</a>"
    html2 = f"<a class='text-success' href='{reverse_lazy('users:profile', args=(u2.pk,))}'>{u2}</a>"
    
    if method == 'add':
        u1.requested.add(u2)
        Notification.objects.create(text=f"{html2} wants to be friends with you", user=u1)
    elif method == 'deny':
        u1.requested.remove(u2)
    elif method == 'accept':
        u2.requested.remove(u1)
        u2.friend.add(u1)
        Notification.objects.create(text=f"You're friends with {html1} now", user=u2)
        Notification.objects.create(text=f"You're friends with {html2} now", user=u1)
    else:
        u2.friend.remove(u1)
    
    return HttpResponseRedirect(reverse('users:profile', args=(u1.pk,)))

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
    
class ProfileView(LoginMixn, DetailView, UpdateView):
    template_name = 'users/profile.html'
    context_object_name = 'userp'
    form_class = UpdateUserForm
    
    def get_object(self, queryset = None):
        if field := self.kwargs.get(self.pk_url_kwarg):
            return get_object_or_404(get_user_model(), pk=field)
        elif field := self.kwargs.get(self.slug_url_kwarg):
            return get_object_or_404(get_user_model(), username=field)
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['title'] = context[self.context_object_name].username
        
        return context