from django.conf.urls import url
from blog import views

#app_name =  'blog'

urlpatterns = [
    # class-based views have an as_view() class method which returns a function that can be called
    # when a request arrives for a URL matching the associated pattern.
    url(r'^$', views.PostListView.as_view(), name= 'post_list'),
    url(r'^about/$', views.AboutView.as_view(), name= 'about'),
    url(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name= 'post_detail'),
    url(r'^post/new/$', views.CreatePostView.as_view(), name= 'post_new'),
    url(r'^post/(?P<pk>\d+)$', views.PostUpdateView.as_view(), name= 'post_edit'),
    url(r'^post/(?P<pk>\d+)$', views.PostDeleteView.as_view(), name= 'post_remove'),
    url(r'^drafts/$', views.DraftListView.as_view(), name= 'post_draft_list'),
]
