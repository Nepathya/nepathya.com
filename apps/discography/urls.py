from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns
from . import api

web_urls = [

]

api_urls = [
    url(r'^api/genres/$', api.GenreListAPI.as_view()),
    url(r'^api/albums/$', api.AlbumListAPI.as_view()),
    url(r'^api/tracks/$', api.TrackListAPI.as_view()),
    url(r'^api/labels/$', api.LabelListAPI.as_view()),
]

api_urls = format_suffix_patterns(api_urls)

urlpatterns = web_urls + api_urls
