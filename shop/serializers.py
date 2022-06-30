from rest_framework import serializers

from shop.models import Movie


class MovieSerilalizer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'name', 'genres']
