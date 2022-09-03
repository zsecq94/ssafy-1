from cgi import print_environ_usage
import json
from pprint import pprint


def movie_info(movies, genres):
    # print(movies)

    movie_lst = []
    for movie in movies:    
        lst = []

        for aaa in movie.get('genre_ids'): # aaa에 movie의 genre_ids값을 넣는다
            for bbb in genres: # bbb에 genres를 넣는다
                if aaa == bbb.get('id'): # aaa와 bbb의 같은 'id'를
                    lst.append(bbb.get('name')) # lst에 bbb의 'name'으로 넣는다
        
        d = {'id' : movie['id'], 
            'genre_name' : lst, 
            'overview' : movie['overview'], 
            'poster_path' : movie['poster_path'], 
            'title'  : movie['title'], 
            'vote_average'  : movie['vote_average']}

        # print(d)
        movie_lst.append(d) # movie_lst에 d를 추가한다.
        # movie['genre_names'] = d.pop('genre_ids') # d의 'genre_names'을 d의 'genre_ids'로 바꾼다
        # d['genre_names'] = lst

    return movie_lst


    # 여기에 코드를 작성합니다.  
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))