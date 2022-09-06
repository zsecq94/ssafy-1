# sort는 sorted() 와는 다르게 원본 list를 변형시키고, None을 리턴합니다.
a = [9, 5, 25, 63, 36, 91]
b = [42,1,62,2,6,95,235]
print(a) # [9, 5, 25, 63, 36, 91]
print(a.sort()) # None
print(a) # [5, 9, 25, 36, 63, 91]
print(sorted(b)) # [1, 2, 6, 42, 62, 95, 235]
print(b) # [42, 1, 62, 2, 6, 95, 235]


# append는 문자열로 추가할 수 있고 xetend는 문자열로 추가할 때 문자 하나하나를 리스트로 추가한다.
cafe = ['starbucks', 'tomntoms', 'hollys']
print(cafe) # ['starbucks', 'tomntoms', 'hollys']
cafe.append('banapresso')
print(cafe) # ['starbucks', 'tomntoms', 'hollys', 'banapresso']
cafe.extend('ediya')
print(cafe) # ['starbucks', 'tomntoms', 'hollys', 'banapresso', 'e', 'd', 'i', 'y', 'a']

# a와 b의 요소는 같다 요소를 다르게 복사 하려면 slice 연산자[:]를 사용하거나 import copy를 사용해야 한다.
a = [1, 2, 3, 4, 5]
b = a
a[2] = 5
print(a)
print(b)
