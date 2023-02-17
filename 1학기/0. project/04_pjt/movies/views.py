from webbrowser import get
from django.shortcuts import redirect, render
import movies

from movies.models import Movie

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies':movies
    }
    return render(request, 'movies/index.html', context)

def new(request):
    return render(request, 'movies/new.html')

def create(request):
    title = request.POST.get('title')
    audience = request.POST.get('audience')
    release_date = request.POST.get('release_date')
    genre = request.POST.get('genre')
    score = request.POST.get('score')
    poster_url = request.POST.get('poster_url')
    description = request.POST.get('description')

    movie = Movie(title=title, audience=audience, release_date=release_date,
    genre=genre, score=score, poster_url=poster_url, description=description)
    movie.save()

    return redirect('movies:detail', movie.pk)

def detail(request, pk):

    movies = Movie.objects.get(pk=pk)
    context = {
        'movies':movies
    }
    return render(request, 'movies/detail.html', context)

def delete(request, pk):
    movies = Movie.objects.get(pk=pk)
    movies.delete()
    return redirect('movies:index')

def edit(request, pk):
    movies = Movie.objects.get(pk=pk)
    context = {
        'movies':movies
    }
    return render(request, 'movies/edit.html', context)

def update(request, pk):
    title = request.POST.get('title')
    audience = request.POST.get('audience')
    genre = request.POST.get('genre')
    score = request.POST.get('score')
    poster_url = request.POST.get('poster_url')
    description = request.POST.get('description')
    movies = Movie.objects.get(pk=pk)
    
    movies.title = title
    movies.audience = audience
    movies.genre = genre
    movies.score = score
    movies.poster_url = poster_url
    movies.description = description

    movies.save()

    return redirect('movies:detail', movies.pk)