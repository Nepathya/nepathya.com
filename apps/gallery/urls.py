from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.album_list, name='album-list'),
    url(r'^images/(?P<slug>[\w-]+)', views.album_images, name='album-images'),
)
