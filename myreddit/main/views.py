from django.db.models.base import Model as Model
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, View
from .models import Post, Image, Comment, Group
from .forms import CommentForm, AddPostForm, AddGroupForm
from .utils import LoginMixn

searchbar = {
    'post_tag': {'query': 'tags__contains', 'model': Post, 'title': 'Post Tag', 'template': 'main/search_post.html', 'context_name': 'posts'},
    'post_title': {'query': 'text__contains', 'model': Post, 'title': 'Post Title', 'template': 'main/search_post.html', 'context_name': 'posts'},
    'group_title': {'query': 'title__contains', 'model': Group, 'title': 'Group Title', 'template': 'main/search_group.html', 'context_name': 'groups'},
    'username': {'query': 'username__contains', 'model': get_user_model(), 'title': 'Username', 'template': 'main/search_user.html', 'context_name': 'members'},
}

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

def JoinGroupView(request, pk):
    group = Group.objects.get(pk=pk)
    group.members.add(request.user)
    group.save()
    return HttpResponseRedirect(reverse('group', args=(group.pk, )))

def QuitGroupView(request, pk):
    group = Group.objects.get(pk=pk)
    group.members.remove(request.user)
    group.save()
    return HttpResponseRedirect(reverse('group', args=(group.pk, )))

class Home(LoginMixn, ListView):
    template_name = 'main/home.html'
    context_object_name = 'posts'
    extra_context = {'title': 'Home'}

    def get_queryset(self):
        return Post.non_group.all()
    
class SubscriptionsView(Home):
    def get_queryset(self):
        return Post.subscription.get_queryset(self.request.user).all()
    
class AllHomeView(Home):
    def get_queryset(self):
        return Post.objects.all()


class Search(LoginMixn, ListView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Search For ' + searchbar[self.request.GET['type']]['title']
        return context
    
    def get_template_names(self):
        return [searchbar[self.request.GET['type']]['template']]
    
    def get_context_object_name(self, object_list):
        return searchbar[self.request.GET['type']]['context_name']
    
    def get_queryset(self):
        searcher = searchbar[self.request.GET['type']]
        for_filter = {searcher['query']: self.request.GET['inp']}
        
        return searcher['model'].objects.filter(**for_filter)
    
    

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
    template_name = 'main/create.html'
    success_url = reverse_lazy('home')
    extra_context = {'title': 'Create post'}
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
    def form_valid(self, form):
        p = form.save(commit=False)
        p.user = self.request.user
        response = super().form_valid(form)
        
        url = form.cleaned_data.get('url')
        if url:
            Image.objects.create(url=url, post=self.object)
        
        return response

class GroupView(LoginMixn, DetailView):
    template_name = 'main/group.html'
    context_object_name = 'group'
    pk_url_kwarg = 'pk'
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['title'] = context['group'].title
        context['posts'] = context['group'].post.all()
        return context
    
    def get_object(self, queryset = None):
        return get_object_or_404(Group.objects, pk=self.kwargs[self.pk_url_kwarg])
    
class GroupCreateView(LoginMixn, CreateView):
    form_class = AddGroupForm
    template_name = 'main/create.html'
    extra_context = {'title': 'Create group'}
    
    def get_success_url(self):
        g = Group.objects.order_by('pk').last()
        return reverse_lazy('group', args=(g.pk,))
    
    def form_valid(self, form):
        g = form.save(commit=False)
        g.admin = self.request.user
        
        return  super().form_valid(form)

