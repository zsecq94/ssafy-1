import sys; sys.stdin = open('123.txt', 'r')

def asd(v):
    for i in range(1, v+1):
        a = i * i * i
        if a == v:
            return i
        elif a > v:
            return -1
    return -1

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    print(f'#{tc} {asd(N)}')
