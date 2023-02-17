import sys; sys.stdin = open('123.txt', 'r')

def asd(v):
    cnt = 0
    result = ''
    a = 1
    while v:
        if v < 2**-a:
            result += '0'
        else:
            v -= 2**-a
            result += '1'
        cnt += 1
        if cnt > 12:
            return 'overflow'
        else:
            a += 1
    return result

for tc in range(1, int(input())+1):
    N = float(input())
    print(f'#{tc} {asd(N)}')