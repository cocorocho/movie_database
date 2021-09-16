from re import search
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import GenreSerializer, MovieSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Genre, Movie
from rest_framework import status
from django.db.models import Q, manager

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
            movie_name = movie_name.lower()
            try:
                movie = Movie.objects.get(name=movie_name)
                serializer = MovieSerializer(movie, many=False)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Movie.DoesNotExist:
                return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            """
            ### Parameters for querying movies ###

            :param search_index: Index for movies to be queried
            :type search_index: int
            :param release_year_min: Minimum year for movie release date
            :type release_year_min: int
            :param release_year_max: Maximum year for movie release date
            :type release_year_max: int
            :param genres: Genres to be queried
            :type genres: list[str]
            :param score_imdb: Min and Max imdb score to be quieried
            :type score_imdb: list[int]
            :param score_rotten_tomatoes: Min and Max imdb score to be queried
            :type score_rotten_tomatoes: list[int]
            """
            MAX_QUERY_AMOUNT = 30
            search_index = request.GET.get("searchIndex")
            if not search_index:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            search_index = int(search_index)
            target_index = search_index + MAX_QUERY_AMOUNT
            release_year_min = request.GET.get("yearMin")
            release_year_max = request.GET.get("yearMax")
            _genres = request.GET.getlist("genres[]")
            try:
                genres = Genre.objects.filter(name__in=_genres)
            except Genre.DoesNotExist:
                return Response(status=status.HTTP_204_NO_CONTENT)
            score_imdb = request.GET.getlist("scoreImdb[]")
            score_rotten_tomatoes = request.GET.getlist("scoreRottenTomatoes[]")
            try:
                movies = Movie.objects.filter(
                    Q(score_imdb__gte=score_imdb[0], score_imdb__lte=score_imdb[1]) | Q(score_imdb__isnull=True),
                    Q(score_rotten_tomatoes__gte=score_rotten_tomatoes[0], score_rotten_tomatoes__lte=score_rotten_tomatoes[1]) | Q(score_rotten_tomatoes__isnull=True),
                    year__gte=release_year_min,
                    year__lte=release_year_max,                                        
                    genres__in=genres,
                ).distinct()[search_index:target_index]
                if not movies:
                    return Response(status=status.HTTP_204_NO_CONTENT)
                print(movies)
                serializer = MovieSerializer(movies, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Movie.DoesNotExist:
                return Response(status=status.HTTP_204_NO_CONTENT)