from django.contrib import admin
from django.conf.urls import include, url
from studentManagement.views import *
from activityManagement.views import *
from leaveManagement.views import *

urlpatterns = [
    # url('admin/', admin.site.urls),
    url('login/', include("login.urls")),
    url('studentManagement/', include("studentManagement.urls")),
    url('activityManagement/',include("activityManagement.urls", namespace='activityManagement')),
    url('leaveManagement/', include("leaveManagement.urls", namespace='leaveManagement')),
]