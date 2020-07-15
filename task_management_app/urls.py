from django.conf.urls import url
from task_management_app import views
from . import views
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import logout


urlpatterns = [
    url('members/logout/', logout, name='logout'),
    url('members', views.index, name='index'),
    url('members/add/', views.edit, name='add'),
    url(r'^edit/(?P<id>\d+)/$', views.edit, name='edit'),
    url(r'^members/delete/(?P<id>\d+)/$', views.delete, name='delete'),
    url(r'^members/detail/(?P<id>\d+)/$', views.detail, name='detail'),
    url('', views.index, name='index'),


    url('api', views.api, name='Api'),
]