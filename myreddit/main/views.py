from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from .models import Post, Image, Comment, Group
from .forms import CommentForm, AddPostForm, AddGroupForm
from .utils import LoginMixn


def LikePostView(request, pk):
    post = get_object_or_404(Post, id=pk)
    if post.likes.filter(username=request.user.username):
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post', args=(pk,)))

def LikeCommView(request, pk):
    comm = get_object_or_404(Comment, id=pk)
    if comm.likes.filter(username=request.user.username):
        comm.likes.remove(request.user)
    else:
        comm.likes.add(request.user)
    return HttpResponseRedirect(reverse('post', args=(comm.post_id,)))

class Home(LoginMixn, ListView):
    template_name = 'main/home.html'
    context_object_name = 'posts'
    extra_context = {'title': 'Home'}

    def get_queryset(self):
        return Post.objects.all()

class TagHome(Home):
    def get_queryset(self):
        return Post.objects.filter(tags__contains=self.kwargs['tag'])

class ShowPost(LoginMixn, DetailView, CreateView):
    form_class = CommentForm
    template_name = 'main/post_info.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'post'
    extra_context = {'title': 'Post'}
    
    def get_success_url(self):
        return self.request.path
    
    def get_object(self, queyset = None):
        return get_object_or_404(Post.objects, pk=self.kwargs[self.pk_url_kwarg])
    
    def form_valid(self, form):
        p = form.save(commit=False)
        p.user = self.request.user
        p.post = Post.objects.get(pk=self.kwargs[self.pk_url_kwarg])
        return super().form_valid(form)

class CreatePost(LoginMixn, CreateView):
    form_class = AddPostForm
    template_name = 'main/post_create.html'
    success_url = reverse_lazy('home')
    extra_context = {'title': 'Create post'}
    
    def form_valid(self, form):
        p = form.save(commit=False)
        p.user = self.request.user
        response = super().form_valid(form)
        
        Image.objects.create(img=form.cleaned_data.get('img'), post=self.object)
        
        return response

class GroupView(LoginMixn, ListView):
    template_name = 'main/group.html'
    context_object_name = 'posts'
    
    def get_context_data(self, **kwargs: Any):
        context =  super().get_context_data(**kwargs)
        group = Group.objects.filter(pk=self.kwargs['pk'])[0]
        context['title'] = group.title
        context['posts'] = group.post.all()
        context['group'] = group
        return context
    
    def get_queryset(self):
        return Post.objects.filter(group_id = self.kwargs['pk'])
    
class GroupCreateView(LoginMixn, CreateView):
    form_class = AddGroupForm
    template_name = 'main/group_create.html'
    extra_context = {'title': 'Create group'}
    
    def get_success_url(self):
        g = Group.objects.order_by('pk').last()
        return reverse_lazy('group', args=(g.pk,))
    
    def form_valid(self, form):
        g = form.save(commit=False)
        g.admin = self.request.user
        
        return  super().form_valid(form)
    