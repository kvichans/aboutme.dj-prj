"""aboutme URL Configuration

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
from django.conf.urls import url
from django.contrib import admin

from mainapp.views import *

urlpatterns = [
    url(r'^{}/?$'.format(pages['info']['url']),   main,   name='info'),
    url(r'^{}/?$'.format(pages['edu' ]['url']),   edu,    name='edu'),
    url(r'^{}/?$'.format(pages['work']['url']),   work,   name='work'),
    url(r'^{}/?$'.format(pages['joi' ]['url']),   hobby,  name='joi'),
    # url(r'^$',      main,   name='info'),
    # url(r'^edu/$',  edu,    name='edu'),
    # url(r'^work/$', work,   name='work'),
    # url(r'^joi/$',  hobby,  name='joi'),
]
