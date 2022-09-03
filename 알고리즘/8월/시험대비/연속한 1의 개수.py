import sys
sys.stdin = open('123.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))

    maxV = 0
    cnt = 0
    for i in range(N):
        if arr[i] == 1:
            cnt += 1
            if maxV < cnt:
                maxV = cnt
        if arr[i] == 0:
            cnt = 0
    print(f'#{tc} {maxV}')