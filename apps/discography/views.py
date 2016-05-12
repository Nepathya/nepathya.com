from django.shortcuts import render
from django.views import generic

from models import Album, Track


def index(request):
    context = {'albums': Album.objects.all()}
    return render(request, 'index.html', context)


class AlbumList(generic.ListView):
    model = Album


class AlbumDetail(generic.DetailView):
    model = Album


class TrackList(generic.ListView):
    model = Track


class TrackDetail(generic.DetailView):
    model = Track

# def discography(request):
#     context = {'albums': Album.objects.all()}
#     return render(request, 'discography/discography.html', context)

# Create your views here.
