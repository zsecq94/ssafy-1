import requests
from pprint import pprint


def recommendation(title):
    URL = 'https://api.themoviedb.org/3/search/movie'
    params = {
        'api_key': '936dc8401bd304eab508a23e5dc38aa9',
        'language': 'ko',
        'query': title
        }

    response = requests.get(URL, params=params).json()
    try:
        a = response['results'][0]
        b = a['id']
    
        URL1 = f'https://api.themoviedb.org/3/movie/{b}/recommendations'
        params = {
            'api_key': '936dc8401bd304eab508a23e5dc38aa9',
            'language': 'ko'
            }

        response1 = requests.get(URL1, params=params).json()
        c = response1.get('results')
        list_a = []

        for i in c:
            list_a.append(i.get('title'))
        return list_a
    except: return None

        

    # 여기에 코드를 작성합니다.  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
