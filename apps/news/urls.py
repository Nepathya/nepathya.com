from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns
from . import api

web_urls = [

]

api_urls = [
    url(r'^api/news/$', api.NewsListAPI.as_view()),
]

api_urls = format_suffix_patterns(api_urls)

urlpatterns = web_urls + api_urls
