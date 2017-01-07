from django.contrib import messages

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from ..feedback.forms import FeedbackForm


def save_feedback(request):
    if request.POST:
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Thanks for leaving a comment.')
    return HttpResponseRedirect(reverse('home'))

# Create your views here.
