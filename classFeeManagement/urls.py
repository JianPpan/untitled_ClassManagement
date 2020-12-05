from django.conf.urls import url

from classFeeManagement.views import classFeeManagement
from classFeeManagement.views import *

app_name = 'daiLyManagement'

urlpatterns = [
    url(r'^$', classFeeManagement, name="classFeeManagement"),
    url(r'^classFeeAdd/$', classFeeAdd, name="classFeeAdd"),
    url(r'^classFeeUpdated/classFeeUpdated/$', classFeeUpdated, name="classFeeUpdated"),
    url(r'^classFeeUpdate/classFeeDelete/(?P<fid>\w{1,3})/$', classFeeDelete, name="classFeeDelete"),
    url(r'^classFeeUpdate/classFeeSearch/$', classFeeSearch, name="classFeeSearch"),
]
