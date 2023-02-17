import sys; sys.stdin = open('123.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [0] * 24
    cnt = 0
    time = [list(map(int, input().split())) for _ in range(N)]
    time.sort(key=lambda x: x[1])
    for i in range(N):
        for j in range(time[i][0], time[i][1]):
            if arr[j] == 1:
                cnt -= 1
                break
            else:
                arr[j] = 1
        cnt += 1

    print(f'#{tc} {cnt}')

