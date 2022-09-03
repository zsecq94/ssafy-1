T = int(input())
for tc in range(1, T+1):
    N = int(input())
    n1, n2, n3, n4 = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    sumV = 0
    sumC = 0
    for i in range(n1, n3+1):
        for j in range(n2, n4+1):       # 평균값을 먼저 구함
            sumV += arr[i][j]
            sumC += 1
    b = sumV//sumC

    cnt = 0
    for i in range(n1, n3+1):
        for j in range(n2, n4+1):
            if arr[i][j] < b:           # arr[i][j]보다 b가 크면
                while arr[i][j] != b:   # arr[i][j]와 b가 다를동안 1올려주고 cnt += 1
                    arr[i][j] += 1
                    cnt += 1
            elif arr[i][j] > b:         # 위와 반대
                while arr[i][j] != b:
                    arr[i][j] -= 1
                    cnt += 1
    print(f'#{tc} {cnt}')
