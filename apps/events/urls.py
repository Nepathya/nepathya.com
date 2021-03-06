from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns
from . import api, views

web_urls = [
    url(r'^list/$', views.EventList.as_view(), name="events_list"),

]

api_urls = [
    url(r'^api/events/$', api.EventsListAPI.as_view()),
]

api_urls = format_suffix_patterns(api_urls)

urlpatterns = web_urls + api_urls
