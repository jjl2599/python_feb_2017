from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^courses$', views.courses),
    url(r'^deletepage/(?P<id>\d+)$', views.deletepage),
    url(r'^delete/(?P<id>\d+)$', views.delete)
]
