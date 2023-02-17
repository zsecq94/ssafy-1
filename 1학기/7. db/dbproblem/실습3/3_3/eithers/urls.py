from unicodedata import name
from django.urls import path
from . import views


app_name = 'eithers'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('random/', views.random, name='random'),
    path('<int:question_pk>/comment/', views.comment_create, name='comment_create'),
]