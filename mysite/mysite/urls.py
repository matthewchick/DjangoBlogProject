"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
    3. Use namespace
    Typically, they are used to put each application's URLs into their own namespace.
    This prevents the reverse() Django function and
    the {% url %} template function from returning the wrong URL
    because the URL-pattern name happened to match in another app.
    Create a built-in login
    https://simpleisbetterthancomplex.com/tutorial/2016/06/27/how-to-use-djangos-built-in-login-system.html
    1. django.contrib.auth in INSTALLED_APPS in the settings.py
    2. python manage.py createsuperuser
    3. import django.contrib.auth.views in urls.py
    4. By default, the django.contrib.auth.views.login view renders the registration/login.html
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.contrib.auth import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
    url(r'accounts/login/$', views.login, name='login'),
    # url(r'accounts/logout/$', views.logout, name='logout', kwargs={'next_page','/'}),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls))
    ] + urlpatterns
