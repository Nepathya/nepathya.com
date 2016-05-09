from rest_framework import generics

from models import Image, Album
from serializers import ImageSerializer, AlbumSerializer


class ImageListAPI(generics.ListAPIView):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()


class AlbumListAPI(generics.ListAPIView):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()
