#### 1번 오류

```python
# 1번 오류 : related_name을 지정해 주지 않아 충돌하여 발생 related_name을 지정해 주면 됨
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
```

---

#### 2번 오류

```python
# remove와 add가 바뀌었음. 2번오류 해결
            if movie.like_users.filter(pk=request.user.pk).exists():
                movie.like_users.remove(request.user)
            else:
                movie.like_users.add(request.user)
```

---

#### 3번 오류

```python
# 팔로우 대상이 자신이 아니라면 진행, 3번오류 해결
        if person != request.user:
```

---

1. 좋아요 구현

```python
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
```

```python
# 아래 if문을 추가하여 자신의 글에는 좋아요가 안보이게 설정
{% if user != movie.user %}
<form action="{% url 'movies:likes' movie.pk %}" method="post">
  {% csrf_token %}
  {% if user in movie.like_users.all %}
    <input type="submit" value="좋아요 취소" class="btn btn-primary btn-sm">
  {% else %}
    <input type="submit" value="좋아요" class="btn btn-primary btn-sm">
  {% endif %}
</form>
{% endif %}
```

---

2. 팔로우 구현

```python
def follow(request, user_pk):
    # 로그인 하지 않은 유저는 로그인 화면으로 redirect
    if request.user.is_authenticated:
        person = get_object_or_404(get_user_model(), pk=user_pk)
        # 팔로우 대상이 자신이 아니라면 진행, 3번오류 해결
        if person != request.user:
            if person.followers.filter(pk=request.user.pk).exists():
            # if request.user in person.followers.all():
                person.followers.remove(request.user)
            else:
                person.followers.add(request.user)
        return redirect('accounts:profile', person.username)
    return redirect('accounts:login')
```

```python
# 아래 if문을 추가하여 자신의 프로필에서는 팔로우 기능 안보이게 설정
{% if person != request.user %}
  <div> 
    <p>
      팔로잉 : {{ person.followings.all|length }} / 팔로워 : {{ person.followers.all|length }}
    </p>
      <div>
        <form action="{% url 'accounts:follow' person.pk %}" method="POST">
          {% csrf_token %}
          {% if user in person.followers.all %}
            <button class="btn btn-outline-primary btn-sm">팔로우 취소</button>
          {% else %}
            <button class="btn btn-primary btn-sm">팔로우</button>
          {% endif %}
        </form>
      </div>
  </div>
{% endif %}
```
