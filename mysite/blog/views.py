from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# https://docs.djangoproject.com/en/2.0/topics/auth/default/
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from blog.models import Post, Comment
from blog.forms import PostForm, CommentForm
from django.views.generic import (TemplateView, ListView, DetailView,CreateView, UpdateView, DeleteView)
# use class based views
# https://docs.djangoproject.com/en/2.0/topics/class-based-views/generic-editing/
# The relationship and history of generic views, class-based views, and class-based generic viewsc
# https://docs.djangoproject.com/en/2.0/topics/class-based-views/intro/
class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = Post
    # https://docs.djangoproject.com/en/2.0/topics/db/queries/
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now().order_by('-published_date'))
        # select * from blog_posts where published_date <= timezone.now() order by published_date

class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    model = Post
    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')

class PostDetailView(DetailView):
    model = Post

class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')
