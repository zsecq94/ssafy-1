from rest_framework import status
from telnetlib import STATUS
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, render
from .models import Actor, Movie, Review
from .serializers import ActorListSerializer, ActorSerializer, MovieListSerializer, MovieSerializer, ReviewDetailSerializer, ReviewSerializer


# Create your views here.

@api_view(['GET'])
def actor_list(request):
    if request.method == 'GET':
        actors = Actor.objects.all()
        serializer = ActorListSerializer(actors, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def actor_detail(request, actor_pk):
    actor = get_object_or_404(Actor, pk=actor_pk)
    serializer = ActorSerializer(actor)
    return Response(serializer.data)


@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        ser = MovieListSerializer(movies, many=True)
        return Response(ser.data)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    ser = MovieSerializer(movie)
    return Response(ser.data)


@api_view(['GET'])
def review_list(request):
    if request.method == 'GET':
        review = Review.objects.all()
        ser = ReviewSerializer(review, many=True)
        return Response(ser.data)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        ser = ReviewDetailSerializer(review)
        return Response(ser.data)
    elif request.method == 'DELETE':
        review.delete()
        context = {
            'delete': f'{review_pk}번 리뷰가 삭제되었습니다.'
        }
        return Response(context, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        ser = ReviewDetailSerializer(review, data=request.data)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response(ser.data)

@api_view(['POST'])
def create_review(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    ser = ReviewDetailSerializer(data=request.data)
    if ser.is_valid(raise_exception=True):
        ser.save(movie=movie)
        return Response(ser.data, status=status.HTTP_201_CREATED)