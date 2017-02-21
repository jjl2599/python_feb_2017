from django.conf.urls import url
from  . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create_user$', views.registration),
    url(r'^registered$', views.registered),
]
