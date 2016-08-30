from rest_framework import generics
from .models import Video
from nepathya.utils import CustomPagination
from .serializers import VideoSerializer


class VideoListAPI(generics.ListAPIView):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()
    pagination_class = CustomPagination