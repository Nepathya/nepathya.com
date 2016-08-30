from rest_framework import generics

from .models import Event
from .serializers import EventSerializer


class EventsListAPI(generics.ListAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
