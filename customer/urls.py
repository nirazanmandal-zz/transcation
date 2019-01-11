from django.conf.urls import url
from . import views

app_name = "customer"

urlpatterns = [
    url(r'^$', views.create, name="create"),
    url(r'^list/$', views.list, name="list"),
    url(r'^update/(?P<pk>\d+)$', views.update, name="update"),
    url(r'^delete/(?P<pk>\d+)$', views.delete, name="delete"),
]
