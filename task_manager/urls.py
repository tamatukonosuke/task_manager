from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^task_management_app/', include(('task_management_app.urls','task_management_app'))),
]
