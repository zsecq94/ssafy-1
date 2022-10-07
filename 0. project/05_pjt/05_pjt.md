# 05_pjt
---
## 느낀점
- 아직 views, models, forms를 작성하기 어려웠고, 익숙하지 않았지만 5번째 관통 프로젝트를 진행하면서 생각하며 작성하다 보니 전보다 많이 익숙해졌다고 생각한다. 작성할때 이해하기 위해 하나하나 뜯어보며 작성했던 부분이 도움이 된 것 같다. 아직 로그인 기능이나 관리자 페이지 관리는 학습은 많이 미흡하다고 생각한다. 주말에 충분히 학습해서 다음주 학습을 위해 준비해야겠다.
---
## INDEX
![ex_screenshot](1.%20index.png)

```python
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'movies/index.html', context)
```
---
## CREATE
![ex_screenshot](2.%20create_1.png)
```python
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = MovieForm()
    context = {
        'form':form,
    }
    return render(request, 'movies/create.html', context)
```
---
## DETAIL
![ex_screenshot](4.%20detail.png)
```python
def detail(request, pk):
    movies = Movie.objects.get(pk=pk)
    context = {
        'movies': movies,
    }
    return render(request, 'movies/detail.html', context)
```
---
## UPDATE
![ex_screenshot](5.%20update.png)
```python
def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm(instance=movie)
    context = {
        'form': form,
        'movie': movie,
    }
    return render(request, 'movies/update.html', context)
```
---
## DELETE 후
![ex_screenshot](6.%20delete.png)
```python
def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return redirect('movies:index')
```