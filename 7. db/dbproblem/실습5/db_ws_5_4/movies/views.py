from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import (
    require_http_methods,
    require_POST,
    require_safe,
)
from django.contrib.auth.decorators import login_required
from .models import Movie, Comment, Hashtag
from .forms import MovieForm, CommentForm


@require_safe
def index(request):
    movies = Movie.objects.order_by("-pk")

    context = {
        "movies": movies,
    }
    return render(request, "movies/index.html", context)


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            for word in movie.content.split():
                if word.startswith('#'):
                   hashtag, created = Hashtag.objects.get_or_create(content=word)
                   movie.hashtags.add(hashtag)
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = {
        'form': form,
    }
    return render(request, 'movies/create.html', context)


@require_safe
def detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    comment_form = CommentForm()
    comments = movie.comment_set.all()
    context = {
        "movie": movie,
        "comment_form": comment_form,
        "comments": comments,
    }
    return render(request, "movies/detail.html", context)


@require_POST
def delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.user.is_authenticated:
        if request.user == movie.user:
            movie.delete()
            return redirect("movies:index")
    return redirect("movies:detail", movie.pk)


@login_required
@require_http_methods(["GET", "POST"])
def update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.user == movie.user:
        if request.method == "POST":
            form = MovieForm(request.POST, instance=movie)
            if form.is_valid():
                form.save()
                return redirect("movies:detail", movie.pk)
        else:
            form = MovieForm(instance=movie)
    else:
        return redirect("movies:index")
    context = {
        "movie": movie,
        "form": form,
    }
    return render(request, "movies/update.html", context)


@require_POST
def comments_create(request, pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.movie = movie
            comment.user = request.user
            comment.save()
        return redirect("movies:detail", movie.pk)
    return redirect("accounts:login")


@require_POST
def comments_delete(request, movie_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect("movies:detail", movie_pk)


@require_POST
def likes(request, movie_pk):
    # 로그인하지 않은 유저는 로그인 화면으로 redirect
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)
        # 좋아요를 누르는 유저와 게시글의 작성자가 다르면
        if movie.user != request.user:
            # remove와 add가 바뀌었음. 2번오류 해결
            if movie.like_users.filter(pk=request.user.pk).exists():
                movie.like_users.remove(request.user)
            else:
                movie.like_users.add(request.user)
        return redirect("movies:index")
    return redirect("accounts:login")


@login_required
def hashtag(request, hash_pk):
    hashtag = get_object_or_404(Hashtag, pk=hash_pk)
    movies = hashtag.movie_set.order_by('-pk')
    context = {
        'hashtag': hashtag, 
        'movies': movies,
    }
    return render(request, 'movies/hashtag.html', context)
