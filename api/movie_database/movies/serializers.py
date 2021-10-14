from rest_framework import serializers
from .models import Language, Movie, Genre, Poster


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["name"]


class PosterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poster
        fields = ["path"]


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ["name"]


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(read_only=True, many=True)
    poster = PosterSerializer(read_only=True, many=False)
    language = LanguageSerializer(read_only=True, many=False)

    class Meta:
        model = Movie
        fields = "__all__"