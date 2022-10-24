from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404

from .serializers import BookListSerializer, BookSerializer, CommentSerializer
from .models import Book, Comment

@api_view(['GET', 'POST'])
def book_list(request):
    # Q 1.
    if request.method == 'GET':
        books = get_object_or_404(Book)
        serializer = BookListSerializer(books)
        return Response(serializer.data)
    # Q 2.
    elif request.method == 'POST':
        books = get_object_or_404(Book)
        serializer = BookSerializer(books)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def book_detail(request, book_pk):
    # Q 3.
    books = Book.objects.get(pk=book_pk)
    if request.method == 'GET':
        serializer = BookSerializer(books)
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)
    # Q 4.
    elif request.method == 'DELETE':
        serializer = BookSerializer(books)
        serializer.delete()
        context = {
            'delete': f'{book_pk}번 게시글이 삭제되었습니다.'
        }
        return Response(context, serializer.data, status=status.HTTP_404_NOT_FOUND)
    # Q 5.
    elif request.method == 'PUT':
        serializer = BookSerializer(books)
        if serializer.is_valid(raise_exception=True):
            serializer.save(serializer=serializer)
            return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def comment_list(request):
    # Q 7.
    if request.method == 'GET':
        comments = get_object_or_404(Comment)
        serializer = CommentSerializer(comments, read_only=True)
        return Response(serializer.data)


@api_view(['POST'])
def comment_create(request, book_pk):
    # Q 8.
    pass

@api_view(['GET', 'DELETE'])
def comment_detail(request, comment_pk):
    # Q 9.
    comments = Comment.objects.get(pk=comment_pk)
    if request.method == 'GET':
        pass

    # Q 10.
    if request.method == 'DELETE':
        serializer = CommentSerializer(comments)
        serializer.delete()
        context = {
            'delete': f'{comment_pk}번 댓글이 삭제되었습니다.'
        }
        return Response(serializer.data, context, status=status.HTTP_404_NOT_FOUND)