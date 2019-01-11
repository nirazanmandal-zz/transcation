from django.conf.urls import url
from . import views

app_name = "units"

urlpatterns = [
    url(r'^$', views.list, name="list"),
    # url(r'^$', views.detail, name="detail"),
    url(r'^create/$', views.create, name="create"),
    url(r'^update/(?P<pk>\d+)/$', views.update, name="update"),
    url(r'^delete/(?P<pk>\d+)/$', views.delete, name="delete"),
    url(r'^list/$', views.list, name="list"),

]

