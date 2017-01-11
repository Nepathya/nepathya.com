from django.shortcuts import render
from django.views import generic
from ..events.models import Event


class EventList(generic.ListView):
    model = Event

# Create your views here.
