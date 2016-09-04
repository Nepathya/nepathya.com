from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns
from . import api
from . import views

web_urls = [
]

api_urls = [
    url(r'^api/feedbacks/$', api.FeedbackCreateAPI.as_view()),
]

api_urls = format_suffix_patterns(api_urls)

urlpatterns = web_urls + api_urls
