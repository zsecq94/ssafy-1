import json


def dec_movies(movies):
    pass 
    bbb = []
    for movie in movies:
        t = movie.get('id')
        t1 = f'data/movies/{t}.json'
        
        movies_json = open(t1, encoding='utf-8')
        movies_list = json.load(movies_json)
        if movies_list.get('release_date')[5:7] == '12':
            bbb.append(movies_list.get('title'))
    
    return bbb
            


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
