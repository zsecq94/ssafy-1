import sys
sys.stdin = open('123.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) + [0] for _ in range(N)]
    # 세로 계산할때 필요한 리스트 생성
    arr.append([0]*N)
    cnt = 0

    # 가로 계산
    for i in range(N):
        sumV = 0
        for j in range(N+1):

            # arr[i][j]가 1이면 sumV에 1더하고
            if arr[i][j] == 1:
                sumV += 1

                # sumV가 K랑 같고 arr[i][j]의 오른쪽이 0이면 카운트 추가하고 섬 초기화
                if sumV == K and arr[i][j+1] == 0:
                    cnt += 1
                    sumV = 0

            # arr[i][j]가 0이면 섬 초기화
            elif arr[i][j] == 0:
                sumV = 0

    # 세로 계산
    for k in range(N):
        sumV1 = 0
        for p in range(N):
            # arr[p][k]가 1이면 섬에 1더함
            if arr[p][k] == 1:
                sumV1 += 1

                # 섬이 K랑 강고 arr[p][k]의 아래가 0이면 카운트 추가하고 섬 초기화
                if sumV1 == K and arr[p+1][k] == 0:
                    cnt += 1
                    sumV1 = 0

            # 0이면 섬 초기화
            elif arr[p][k] == 0:
                sumV1 = 0

    print(f'#{tc} {cnt}')