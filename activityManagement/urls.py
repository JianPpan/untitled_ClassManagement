from django.conf.urls import url

from activityManagement.views import *

app_name = 'dailyManagement'

urlpatterns = [
    url(r'^$', activityManagement, name="activityManagement"),
    url(r'^activityAdd/$', activityAdd, name="activityAdd"),
    url(r'^activityUpdate/activityUpdated/$', activityUpdated, name="activityUpdated"),
    url(r'^activityUpdate/activityDelete/(?P<aid>\w{1,13})/$', activityDelete, name="activityDelete"),
    url(r'^activityUpdate/activitySearch/$', activitySearch, name="activitySearch"),
]
