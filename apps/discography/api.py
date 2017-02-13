from rest_framework import generics

from .models import Label, Track, Album, Genre
from .serializers import LabelSerializer, TrackSerializer, AlbumSerializer, GenreSerializer


class LabelListAPI(generics.ListAPIView):
    serializer_class = LabelSerializer
    queryset = Label.objects.all()


class TrackListAPI(generics.ListAPIView):
    serializer_class = TrackSerializer
    queryset = Track.objects.all()

    def get_queryset(self):
        if 'single_track' in self.request.GET:
            tracks = Track.objects.filter(album__isnull=True)
            return self.serializer_class(tracks, many=True).data
        return super(TrackListAPI, self).get_queryset()


class AlbumListAPI(generics.ListAPIView):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()


class AlbumDetailAPI(generics.RetrieveAPIView):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()


class GenreListAPI(generics.ListAPIView):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
