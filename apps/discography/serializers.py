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
    name = serializers.ReadOnlyField(source='social_icon.name')

    class Meta:
        model = MusicStore
        exclude = ()



class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True)
    album_music_store = MusicStoreSerializer(many=True)

    class Meta:
        model = Album
        exclude = ()
