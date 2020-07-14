from django.conf.urls import url
from task_management_app import views
from . import views
from django.urls import path
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^$', views.hello_world, name='hello_world'),
    path('index', views.index, name='index'),
    url('api', views.api, name='Api'),
]