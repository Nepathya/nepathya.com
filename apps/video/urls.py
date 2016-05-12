from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns
from . import api, views

web_urls = [
    url(r'^$', views.VideoList.as_view(), name="video_list"),
    url(r'^(?P<pk>\d+)/$', views.VideoDetail.as_view(), name="video_detail"),
]

api_urls = [

]

api_urls = format_suffix_patterns(api_urls)

urlpatterns = web_urls + api_urls
