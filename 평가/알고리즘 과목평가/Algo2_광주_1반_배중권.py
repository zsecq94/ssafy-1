T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sam = [list(map(int, input().split())) for _ in range(3)]

    sumA = 0
    for i in range(3):              # 패턴의 1의 개수를 먼저 구함
        for j in range(3):
            sumA += sam[i][j]

    cnt = 0
    for i in range(N-2):
        for j in range(N-2):
            sumV = 0
            for k in range(3):
                for p in range(3):
                    if arr[i+k][j+p] == 1 and sam[k][p] == 1:
                        sumV += 1
            if sumA == sumV:        # 패턴의 1의 개수와 sumV가 같다면 cnt += 1
                cnt += 1
    print(f'#{tc} {cnt}')