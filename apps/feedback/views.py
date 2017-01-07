from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from ..feedback.forms import FeedbackForm


def save_feedback(request):
    if request.POST:
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
    return HttpResponseRedirect(reverse('home'))

# Create your views here.
