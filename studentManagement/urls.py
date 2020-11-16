from django.conf.urls import url

from studentManagement.views import *

app_name = 'statusManagement'

urlpatterns = [
    url(r'^$', studentManagement, name="studentManagement"),
    url(r'^studentAdd/$', studentAdd, name="studentAdd"),
    url(r'^studentUpdate/studentUpdated/$', studentUpdated, name="studentUpdated"),
    url(r'^studentUpdate/studentDelete/(?P<sno>\w{1,13})/$', studentDelete, name="studentDelete"),
    url(r'^studentUpdate/studentSearch/$', studentSearch, name="studentSearch"),
]
