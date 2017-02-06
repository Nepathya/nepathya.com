from django.shortcuts import render
from django.views import generic
from ..video.models import Video

from .models import Album, Track


def index(request):
    context = {'video_object_list': Video.objects.all().order_by('-pk')[:3]}
    return render(request, 'index.html', context)


class AlbumList(generic.ListView):
    model = Album

    def get_context_data(self, **kwargs):
        context = super(AlbumList, self).get_context_data(**kwargs)
        single_tracks = Track.objects.filter(album__isnull=True)
        context['single_tracks'] = single_tracks
        return context


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
