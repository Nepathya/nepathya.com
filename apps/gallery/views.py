from django.shortcuts import render
from django.views import generic

from .models import Image, Album



class AlbumList(generic.ListView):
    model = Album


class AlbumDetail(generic.DetailView):
    model = Album

# Create your views here.
