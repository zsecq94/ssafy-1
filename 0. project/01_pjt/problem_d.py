import json
from typing import AsyncContextManager


def max_revenue(movies):
    pass
    maxV = 0
    # 여기에 코드를 작성합니다.  
    for movie in movies:
        t = movie.get('id')
        t1 = f'data/movies/{t}.json'

        movies_json = open(t1, encoding='utf-8')
        movies_list = json.load(movies_json)
        a = movies_list.get('revenue') # a에서 리베뉴값을 하나 가져온다
        if maxV < a: # a의 값이 maxV보다 크면
            maxV = a # a는 maxV
            title = movies_list.get('title') # 'movies_list.get('title')를 title에 저장
        
    return title
        
    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))
