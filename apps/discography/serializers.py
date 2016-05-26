from rest_framework import serializers
from .models import Label, Genre, Album, Track


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        exclude = ()


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        exclude = ()


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        exclude = ()


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        exclude = ()