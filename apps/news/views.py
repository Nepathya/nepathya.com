from django.views import generic
from .models import News


class NewsList(generic.ListView):
    model = News


class NewsDetail(generic.DetailView):
    model = News
