from rest_framework import serializers
from .models import Actor, Movie, Review


class ActorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = '__all__'

    
class MovieTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title',)


class ActorSerializer(serializers.ModelSerializer):
    movies = MovieTitleSerializer(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = '__all__'


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'overview',)

class ActorNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('name',)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('title', 'content',)


class MovieSerializer(serializers.ModelSerializer):
    actors = ActorNameSerializer(many=True, read_only=True)
    review_set = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'


class ReviewDetailSerializer(serializers.ModelSerializer):
    movie = MovieTitleSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'