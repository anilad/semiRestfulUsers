from django.conf.urls import url, include
from . import views
import re

urlpatterns = [
    url(r'^$', views.index),
    url(r'^users/$', views.index),
    url(r'^users/new$', views.new),
    url(r'^users/create$', views.create),
    url(r'^users/(?P<number>[0-9])$', views.show),
    url(r'^users/(?P<number>[0-9])/edit$', views.edit),
    url(r'^users/(?P<number>[0-9])/update$', views.update),
    url(r'^users/(?P<number>[0-9])/delete$', views.destroy),
]