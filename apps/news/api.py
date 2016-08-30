from rest_framework import generics

from .models import News
from nepathya.utils import CustomPagination
from .serializers import NewsSerializer


class NewsListAPI(generics.ListAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all()
    pagination_class = CustomPagination
