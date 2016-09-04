from rest_framework import generics

from .models import Feedback
from .serializers import FeedbackSerializer


class FeedbackCreateAPI(generics.ListCreateAPIView):
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
