from rest_framework.generics import (
    ListCreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)

from shop.models import Movie
from shop.serializers import MovieSerilalizer


class MyView(ListCreateAPIView):
    serializer_class = MovieSerilalizer
    queryset = Movie.objects.all()


class MovieRetrieveUpdateView(RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerilalizer
    queryset = Movie.objects.all()
