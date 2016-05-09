from django.conf.urls import url

from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from . import api

web_urls = [
    url(r'^$', views.album_list, name='album-list'),
    url(r'^images/(?P<slug>[\w-]+)', views.album_images, name='album-images'),
]

api_urls = [
    url(r'^api/images/$', api.ImageListAPI.as_view()),
    url(r'^api/albums/$', api.AlbumListAPI.as_view()),
]

api_urls = format_suffix_patterns(api_urls)

urlpatterns = web_urls + api_urls
