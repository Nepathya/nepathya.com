from django.contrib import admin
from .models import Track, Album, Label, Genre, MusicStore

admin.site.register(Track)
admin.site.register(Album)
admin.site.register(Label)
admin.site.register(Genre)
admin.site.register(MusicStore)
# admin.site.register(Discography)

# Register your models here.
