from django.contrib import admin
from django.urls import path, re_path
from . import views
from django.conf.urls import include
from django.views.generic.base import RedirectView

urlpatterns = [

    path('', views.index, name='index'),
    path('myblob', views.myblob, name='myblob'),
]