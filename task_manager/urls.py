from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from django.contrib.auth.views import logout

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')), 
    url(r'^admin/', admin.site.urls),
    url('', include(('task_management_app.urls','task_management_app'))),
    url(r'^task_management_app/', include(('task_management_app.urls','task_management_app'))),
]
