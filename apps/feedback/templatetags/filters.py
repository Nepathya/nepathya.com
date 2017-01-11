from django import template
from django.apps import apps
from django.template import TemplateSyntaxError, Node
from django.conf import settings
from apps.feedback.forms import FeedbackForm

register = template.Library()


@register.assignment_tag
def feedback_form(string):
    return FeedbackForm()


@register.assignment_tag
def google_api_key():
    return settings.GOOGLE_API_KEY


def strip_quotes(string):
    if string is None:
        return None
    if string.startswith('"') and string.endswith('"'):
        string = string[1:-1]

    if string.startswith("'") and string.endswith("'"):
        string = string[1:-1]

    return string


class LatestContentNode(Node):
    def __init__(self, model, num, order_by, varname):
        self.num, self.varname, self.order_by = num, varname, strip_quotes(order_by)
        self.model = apps.get_model(*model.split('.'))

    def render(self, context):

        if self.order_by:
            context[self.varname] = self.model._default_manager.all().order_by(self.order_by)[:int(self.num)]
        else:
            context[self.varname] = self.model._default_manager.all()[:self.num]
        return ''


@register.tag
def get_latest(parser, token):
    bits = token.contents.split()
    if len(bits) is 6:
        return LatestContentNode(bits[1], bits[2], bits[3], bits[5])
    elif len(bits) is 5:
        return LatestContentNode(bits[1], bits[2], None, bits[4])
    else:
        raise TemplateSyntaxError("invalid number of arguments")

