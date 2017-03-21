"""oversigt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import (
	password_reset,
	password_reset_done,
	password_reset_confirm,
	password_reset_complete
	)

from madplan import views
from madplan.backends import MyRegistrationView

from django.template.defaultfilters import slugify

urlpatterns = [
    url(r'^$', views.index, name="home"),
    url(r'^about/$', views.about, name="about"),
    url(r'^contact/$', views.contact, name="contact"),

    url(r'^dishes/(?P<slug>[-\w]+)/$', views.dish_detail, name='dish_detail'),
    url(r'^dishes/(?P<slug>[-\w]+)/edit/$', views.edit_dish, name='edit_dish'),
    
    # the new password reset URLs
    url(r'^accounts/password/reset/$', 
        password_reset,
        {'template_name':
        'registration/password_reset_form.html'},
        name="password_reset"),
    url(r'^accounts/password/reset/done/$',
        password_reset_done,
        {'template_name':
        'registration/password_reset_done.html'},
        name="password_reset_done"),    
    url(r'^accounts/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 
        password_reset_confirm,
        {'template_name':
        'registration/password_reset_confirm.html'},
        name="password_reset_confirm"),    
    url(r'^accounts/password/done/$', 
        password_reset_complete,
        {'template_name':
        'registration/password_reset_complete.html'},
        name="password_reset_complete"),

    # registration urls
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^accounts/create_dish/$', views.create_dish,
        name='registration_create_dish'),
    url(r'^accounts/register/$',
        MyRegistrationView.as_view(), name='registration_register'),
    
    url(r'^admin/', admin.site.urls),
]