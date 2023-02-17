# 06_pjt_README

###### 짧은시간에 집중해서 구현했다.  기억이 안나거나 잘 모르겠던 부분들은 전에 했던 프로젝트를 참고하여 작성했는데 기억이 안나는 부분이 많았다. 그날 했던 수업들을 md파일로 하나하나 기록하고 복습하는 습관을 들여야 겠다고 생각했다.

---

1. index 구현

```python
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'movies/index.html', context)
```

```html
{% extends 'base.html' %}

{% block content %}
  <h1>INDEX</h1>
  <a href="{% url 'movies:create' %}" >[CREATE]</a>
  <hr>
  {% for movie in movies %}
    <p><a href="{% url 'movies:detail' movie.pk %}">{{ movie.title }}</a></p>
  {% endfor %}
{% endblock content %}

```

![](assets/a5fed8f714284942da8962831048f34eefee9794.PNG)

---

2. detail 구현

```python
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
```

```html
{% extends 'base.html' %}

{% block content %}
  <h1>DETAIL</h1>
  <hr>
  
  <h4>{{ movie.title }}</h4>
  <h6>{{ movie.description }}</h6>

  <a href="{% url 'movies:update' movie.pk %}">UPDATE</a>
  <form action="{% url 'movies:delete' movie.pk %}">
    <input type="submit" value="DELETE">
  </form>
  <a href="{% url 'movies:index' %}">BACK</a>
  <hr>
  <h4>댓글 목록</h4>
  {% for comment in comments %}
    <li>{{ comment.content }}</li>
  {% endfor %}
  <hr>
  {% if request.user.is_authenticated %}
    <form action="{% url 'movies:comments_create' movie.pk %}" method="POST">
      {% csrf_token %}
      {{ comment_form.as_p }}<input type="submit">
    </form>
  {% endif %}
{% endblock content %}

```

![](assets/05f2d6c4820f4e5db6fe8bb8a3ed17d36efa4da6.PNG)

---

3. create 구현

```python
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = {
        'form': form
    }
    return render(request, 'movies/Create.html', context)
```

```html
{% extends 'base.html' %}

{% block content %}
  <h1>CREATE</h1>
  <hr>
  <form action="{% url 'movies:create' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Submit">
  </form>
  <hr>

  <a href="{% url 'movies:index' %}">BACK</a>
{% endblock content %}

```

![](assets/61dc50d8cde14aa6b87c760d5d2ec8296cf8ed2e.PNG)

---

4. update 구현

```python
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
```

```html
{% extends 'base.html' %}

{% block content %}
  <h1>UPDATE</h1>
  <form action="{% url 'movies:update' movie.pk %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="reset" value="Reset">
    <input type="submit" value="Submit">
  </form>
  <hr>
  <a href="{% url 'movies:index' %}">BACK</a>
{% endblock content %}
```

![](assets/c21de368c311586406d4b066d2e8c6e249447432.PNG)

---

5. login, logout 구현

```python
def login(request):
    if request.user.is_authenticated:
        return redirect('movies:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'movies:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)
```

```html
{% extends 'base.html' %}

{% block content %}
  <h1>Login</h1>
  <form action="" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Submit">
  </form>
{% endblock content %}

```

```python
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('movies:index')
```

![](assets/2690e76fb858fa665788378269bde2aa27d8d297.PNG)

---

6. signup 구현

```python
def signup(request):
    if request.user.is_authenticated:
        return redirect('movies:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('movies:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)
```

```html
{% extends 'base.html' %}

{% block content %}
  <h1>Signup</h1>
  <form action="{% url 'accounts:signup' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Submit">
  </form>
{% endblock content %}
```

![](assets/0c559be916f71c8c9a044c4f94acd308520d58af.PNG)

---

7. update 구현

```python
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)
```

```html
{% extends 'base.html' %}

{% block content %}
  <h1>회원정보수정</h1>
  <form action="{% url 'accounts:update' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Submit">
  </form>
{% endblock content %}
```

![](assets/b1da835ef82dd26ae3f059eff8179fd2ed4d294f.PNG)

---

8. change_password 구현

```python
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('movies:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)
```

```html
{% extends 'base.html' %}

{% block content %}
  <h1>비밀번호 변경</h1>
  <form action="{% url 'accounts:change_password' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Submit">
  </form>
{% endblock content %}
```

![](assets/b0143604ccf75d15fd6b1690a74edd5e0087d427.PNG)

---
