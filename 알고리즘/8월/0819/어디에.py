import sys
sys.stdin = open('123.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for row in range(N):
        col = 0
        while col <= N-1:
            while col <= N-1 and arr[row][col] == 0:
                col += 1
            cnt = 0
            while col <= N-1 and arr[row][col] == 1:
                col += 1
                cnt += 1
            if cnt == K:
                result += 1

    for col in range(N):
        row = 0
        while row <= N-1:
            while row <= N-1 and arr[row][col] == 0:
                row += 1
            cnt = 0
            while row <= N-1 and arr[row][col] == 1:
                row += 1
                cnt += 1
            if cnt == K:
                result += 1

    print(f'#{tc} {result}')