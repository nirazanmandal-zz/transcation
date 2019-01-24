from django.conf.urls import url
from . import views

app_name = "txn"

urlpatterns = [
    url(r'^index/$', views.index, name="index"),
    url(r'^list/$', views.list, name="list"),
    url(r'^paid/(?P<pk>\d+)/$', views.paid, name="paid"),
]
