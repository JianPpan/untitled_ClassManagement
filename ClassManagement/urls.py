from django.contrib import admin
from django.conf.urls import include, url
from studentManagement.views import *

urlpatterns = [
    # url('admin/', admin.site.urls),
    url('login/', include("login.urls")),
    url('studentManagement/', include("studentManagement.urls")),
]
