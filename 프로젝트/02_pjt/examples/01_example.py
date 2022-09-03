# requests 사용 예시 1

import requests


URL = 'https://api.themoviedb.org/3/search/movie?api_key=936dc8401bd304eab508a23e5dc38aa9&language=ko'

response = requests.get(URL).json()
print(response)

results = response.get('title')
print(results)
