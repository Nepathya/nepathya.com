from django.shortcuts import render
from django.views import generic

from models import Album


def index(request):
    context = {'albums': Album.objects.all()}
    return render(request, 'index.html', context)


class AlbumList(generic.ListView):
    model = Album
    # queryset = Album.objects.all()


class AlbumDetail(generic.DetailView):
    model = Album

## def discography(request):
#     context = {'albums': Album.objects.all()}
#     return render(request, 'discography/discography.html', context)

# Create your views here.
