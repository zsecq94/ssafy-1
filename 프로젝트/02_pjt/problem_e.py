import requests
from pprint import pprint


def credits(title):
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

        URL1 = f'https://api.themoviedb.org/3/movie/{b}/credits'
        params = {
            'api_key': '936dc8401bd304eab508a23e5dc38aa9',
            'language': 'ko',
            }
        response1 = requests.get(URL1, params=params).json()
        list_a = []
        list_b = []
        dict_a = {}
        a = response1['cast']
        for i in a:
            if i.get('cast_id') < 10:
                list_a.append(i['name'])
        
        b = response1['crew']
        for i in b:
            if i.get('department') == 'Directing':
                list_b.append(i['name'])

        dict_a = {'cast': list_a, 'directing' : list_b}
        return dict_a
    except: return None

    # 여기에 코드를 작성합니다.  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
