from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import GenreSerializer, MovieSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Genre, Movie
from rest_framework import status

# Create your views here.

class GetGenres(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FindMovie(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        movie_name = request.GET.get("movieName")

        if movie_name:
            try:
                movie = Movie.objects.get(name=movie_name)
                serializer = MovieSerializer(movie, many=False)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Movie.DoesNotExist:
                return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            release_year_min = request.GET.get("yearMin")
            release_year_max = request.GET.get("yearMax")
            score_imdb = request.GET.get("scoreIMDB")
            score_rottentomatoes = request.GET.get("scoreRottenTomates")
            try:
                movie = None
            except Movie.DoesNotExist:
                return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)
