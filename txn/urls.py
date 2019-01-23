from django.conf.urls import url
from . import views

app_name = "txn"

urlpatterns = [
    url(r'^index/$', views.index, name="index"),
    url(r'^list/$', views.list, name="list"),

]
