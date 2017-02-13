from rest_framework import generics
from rest_framework.response import Response

from .models import Label, Track, Album, Genre
from .serializers import LabelSerializer, TrackSerializer, AlbumSerializer, GenreSerializer


class LabelListAPI(generics.ListAPIView):
    serializer_class = LabelSerializer
    queryset = Label.objects.all()


class TrackListAPI(generics.ListAPIView):
    serializer_class = TrackSerializer
    queryset = Track.objects.all()


class SingleTrackListAPI(generics.ListAPIView):
    serializer_class = TrackSerializer
    queryset = Track.objects.filter(album__isnull=True)


class AlbumListAPI(generics.ListAPIView):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()


class AlbumDetailAPI(generics.RetrieveAPIView):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()


class GenreListAPI(generics.ListAPIView):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
