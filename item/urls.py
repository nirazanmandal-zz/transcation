from django.conf.urls import url
from . import views

app_name = "item"

urlpatterns = [
    url(r'^$', views.create, name="create"),
    url(r'^list/$', views.list, name="list"),
    url(r'^create/$', views.create, name="create"),
]
