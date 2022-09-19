import sys; sys.stdin = open('123.txt', 'r')

# f = 전체 층 수, s = 지금 있는 층, g = 도착 층
T = int(input())
for tc in range(1, T+1):
    f, s, g, u, d = map(int, input().split())

    cnt = 0
    while s != g:
        if s < g:
            s += u
            cnt += 1
        elif d == 0:
            cnt = 'use the stairs'
            break
        else:
            s -= d
            cnt += 1
    print(cnt)