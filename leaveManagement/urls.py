from django.conf.urls import url

from leaveManagement.views import *

app_name = 'dailysManagement'

urlpatterns = [
    url(r'^$', leaveManagement, name="leaveManagement"),
    url(r'^leaveAdd/$', leaveAdd, name="leaveAdd"),
    url(r'^leaveUpdate/leaveUpdated/$', leaveUpdated, name="leaveUpdated"),
    url(r'^leaveUpdate/leaveDelete/(?P<lid>\w{1,13})/$', leaveDelete, name="leaveDelete"),
    url(r'^leaveUpdate/leaveSearch/$', leaveSearch, name="leaveSearch"),
]
