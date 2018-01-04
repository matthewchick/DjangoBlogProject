from django.shortcuts import render, get_object_or_404, redirect
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
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
        # return Post.objects.filter(published_date__lte=timezone.now().order_by('-published_date'))
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

#######################################
## Functions that require a pk match ##
#######################################
"""
login_required() does the following:

    If the user isn’t logged in, redirect to settings.LOGIN_URL, passing the current absolute path in the query string.
    If the user is logged in, execute the view normally. The view code is free to assume the user is logged in.
    https://docs.djangoproject.com/en/2.0/topics/auth/default/
    https://docs.djangoproject.com/en/2.0/topics/forms/modelforms/
"""
@login_required    #decorators
def post_publish(request, pk):
    # https://docs.djangoproject.com/en/2.0/topics/http/shortcuts/
    post = get_object_or_404(Post, pk=pk)
    post.publish()      #from model post
    return redirect('post_detail', pk=pk)

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)    # Create a form instance with POST data.
        if form.is_valid():
            comment = form.save(commit=False) # Create, but don't save the new author instance.
            comment.post = post  # modify and pass post pk to comment
            comment.save()       # Save the new instance.
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()   # create a new object
    return render(request, 'blog/comment_form.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()      # from model comment
    return redirect('post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)
