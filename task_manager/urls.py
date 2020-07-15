from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from django.contrib.auth.views import logout

urlpatterns = [
    url('todo_list/', include(('todo_list.urls','todo_list'))),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')), 
    url('admin/', admin.site.urls),
    url('task_management_app/', include(('task_management_app.urls','task_management_app'))),
]
