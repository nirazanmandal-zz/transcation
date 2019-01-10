from django.conf.urls import url
from . import views

app_name = "units"

urlpatterns = [
    url(r'^$', views.list, name="list"),
    url(r'^detail/(?P<pk>\d+)$', views.list, name="detail"),
]

