from django.shortcuts import render

from models import Album


def index(request):
    context = {'albums': Album.objects.all()}
    return render(request, 'index.html', context)

#
# def discography(request):
#     context = {'albums': Album.objects.all()}
#     return render(request, 'discography/discography.html', context)

# Create your views here.
