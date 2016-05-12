from django.shortcuts import render
from django.views import generic
from models import Video


class VideoList(generic.ListView):
    model = Video


class VideoDetail(generic.DetailView):
    model = Video