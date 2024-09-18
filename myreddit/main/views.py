from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from .models import Post, Image
from .forms import CommentForm, AddPostForm
from .utils import LoginMixn


def temp(r): return render(r, 'main/home.html')

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
    
    def form_valid(self, form):
        p = form.save(commit=False)
        p.user = self.request.user
        response = super().form_valid(form)
        
        Image.objects.create(img=form.cleaned_data.get('img'), post=self.object)
        
        return response