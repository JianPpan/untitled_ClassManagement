from django.conf.urls import url
from login.views import login


app_name = 'logins'

urlpatterns = [
    url(r'^$', login, name='login')
]