from django.conf.urls import url
from . import views

app_name = "item"

urlpatterns = [
    url(r'^list/$', views.list, name="list"),
    url(r'^create/$', views.create, name="create"),
    url(r'^edit/(?P<pk>\d+)/$', views.edit, name="edit"),
    url(r'^delete/(?P<pk>\d+)/$', views.delete, name="delete"),
]
