from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from todos.serializers import TodoSerializer
from todos.models import Todo
from .serializers import UserSerializer
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
)


@api_view(['POST'])
def signup(request):
    if request.user.is_authenticated:
        todos = Todo.objects.all()
        todoserializer = TodoSerializer(todos, many=True)
        return Response(todoserializer.data)
    
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        password = serializer.initial_data.get('password')

        if serializer.is_valid(raise_exception=True):
            if serializer.validated_data.get('password') == serializer.validated_data.get('password_check'):
                user = serializer.save()
                user.set_password(password)
                user.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)