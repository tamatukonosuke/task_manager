from django.conf.urls import url
from task_management_app import views
from . import views
from django.urls import path
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^$', views.hello_world, name='hello_world'),
    url('index', views.one, name='one'),
    url('api', views.api, name='Api'),



    url(r'^members/$', views.index, name='index'),
    url(r'^members/add/$', views.edit, name='add'),
    url(r'^members/edit/(?P<id>\d+)/$', views.edit, name='edit'),
    url(r'^members/delete/(?P<id>\d+)/$', views.delete, name='delete'),
    url(r'^members/detail/(?P<id>\d+)/$', views.detail, name='detail'),
]