from typing import KeysView
import requests

def popular_count():
    URL = 'https://api.themoviedb.org/3/movie/popular'
    params = {'api_key': '936dc8401bd304eab508a23e5dc38aa9',
                'language': 'ko'}

    response = requests.get(URL, params=params).json()
    a = response['results']
    b = tuple(m['id'] for m in a)
    return len(b)

    
    # 여기에 코드를 작성합니다.  
    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
