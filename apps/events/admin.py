from django.contrib import admin
from ..events.models import Event, Location, TicketLocation

admin.site.register(Location)
admin.site.register(Event)
admin.site.register(TicketLocation)
