from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns
from . import api
from . import views

web_urls = [
    url(r'^album/list/$', views.AlbumList.as_view(), name="album_list"),
    url(r'^album/detail/(?P<pk>\d+)/$', views.AlbumDetail.as_view(), name="album_detail"),
    url(r'^track/list/$', views.TrackList.as_view(), name="track_list"),
    url(r'^track/detail/(?P<pk>\d+)/$', views.TrackDetail.as_view(), name="track_detail"),
]

api_urls = [
    url(r'^api/genres/$', api.GenreListAPI.as_view()),
    url(r'^api/albums/$', api.AlbumListAPI.as_view()),
    url(r'^api/albums/(?P<pk>\d+)/$', api.AlbumDetailAPI.as_view()),
    url(r'^api/tracks/$', api.TrackListAPI.as_view()),
    url(r'^api/single_tracks/$', api.SingleTrackListAPI.as_view()),
    url(r'^api/labels/$', api.LabelListAPI.as_view()),
]

api_urls = format_suffix_patterns(api_urls)

urlpatterns = web_urls + api_urls
