import sys
sys.stdin = open('123.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result_90 = [[] * N for _ in range(N)]
    result_180 = [[] * N for _ in range(N)]
    result_270 = [[] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            result_90[j].append(arr[N-i-1][j])

    for i in range(N):
        for j in range(N):
            result_180[j].append(result_90[N-i-1][j])

    for i in range(N):
        for j in range(N):
            result_270[j].append(result_180[N-i-1][j])

    print(f'#{tc}')
    for i in range(N):
        print(''.join(map(str, result_90[i])), ''.join(map(str, result_180[i])), ''.join(map(str, result_270[i])))