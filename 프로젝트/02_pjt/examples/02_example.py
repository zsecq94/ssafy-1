# requests 사용 예시 2

import requests


URL = 'https://api.themoviedb.org/3/movie/{movie_id}/recommendations'

params = {
    'api_key': '936dc8401bd304eab508a23e5dc38aa9',
    'language': 'ko'
}

response = requests.get(URL, params=params).json()
print(response)
