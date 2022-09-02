# 문자열 뒤집기 : 'abcd' s[::-1]
'''
def reverseA(s):
    s = list(s)
    N = len(s)
    for i in range(N//2):
        s[i], s[N-1-i] = s[N-1-i], s[i]
    s = ''.join(s)
    return s

print(reverseA('abcd'))
-------------------------
s1= 'abc'
s2= 'abc'
s3= 'def'
s4= s1
s5= s1[:2] + 'c'
print(s1 == s2, s1 is s2)
print(s1 == s3, s1 is s3)
print(s1 == s4, s1 is s4)
print(s1, s5)
print(s1 == s5, s1 is s5)
-------------------------
def my_strcmp(str1, str2):
    if str1 > str2:
        return -1
    elif str1 < str2:
        return 1
    else:
        return 0

print(my_strcmp('abcd', 'b'))
print(my_strcmp('b', 'abcd'))
print(my_strcmp('abcd', 'abcd'))
--------------------------
# def atoi(s):
#     i = 0
#     for x in s:
#         i = i*10 + ord(x) - ord('0')
#     return i
#
# print(atoi('123'))
---------------------------
# chr(x + ord('0'))
def str_a(s):
    i = ''
    while s > 0:
        i = chr(s % 10 + ord('0')) + s
        s //= 10
    return i

print(str_a(123))
print(str_a(321))
----------------------------
# 찾으면 패턴의 시작위치를 return 하고
# 못찾으면 -1을 return
def find(t, p):
    i = 0
    j = 0
    while j < M and i < N :
        if t[i] != p[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
    if j == M:
        return i-M
    else:
        return -1

t = 'a pattern matching algorithm test'
p = 'test'
N = len(t)
M = len(p)
print(find(t, p))
-----------------------------
'''
