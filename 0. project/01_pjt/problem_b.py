import json
from pprint import pprint 
import problem_a


def movie_info(movie, genres):
    d = problem_a.movie_info(movie)
    lst = []
    for aaa in d.get('genre_ids'): # aaa에 d의 genre_ids값을 넣는다
        for bbb in genres: # bbb에 genres를 넣는다
            if aaa == bbb.get('id'): # 만약 aaa와bbb의 같은 id를
                lst.append(bbb.get('name')) # lst에 bbb의 'name'으로 넣는다
    # # dictionary[new_key] = dictionary.pop(old_key)
    d['genre_names'] = d.pop('genre_ids') # d의 'genre_names'을 d의 'genre_ids'로 바꾼다
    d['genre_names'] = lst
    return d
    # # 여기에 코드를 작성합니다.  
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
 
 
