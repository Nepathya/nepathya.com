from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns
from . import api

web_urls = [

]

api_urls = [
    url(r'^api/genre/$', api.GenreListAPI.as_view()),
    url(r'^api/album/$', api.AlbumListAPI.as_view()),
    url(r'^api/track/$', api.TrackListAPI.as_view()),
    url(r'^api/label/$', api.LabelListAPI.as_view()),
]

api_urls = format_suffix_patterns(api_urls)

urlpatterns = web_urls + api_urls
