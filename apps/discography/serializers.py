from rest_framework import serializers
from .models import Label, Genre, Album, Track, MusicStore


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        exclude = ()


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        exclude = ()


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        exclude = ()

class MusicStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicStore
        exclude = ()



class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True)
    music_store = MusicStoreSerializer(many=True)

    class Meta:
        model = Album
        exclude = ()
