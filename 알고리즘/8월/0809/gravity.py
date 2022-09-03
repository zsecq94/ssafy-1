T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    maxV = 0  # testcast 마다 초기화
    for i in range(N):  # 기준
        cnt = 0  # arr[i]오른쪽 원소 중 더 작은 원소의 개수
        for j in range(i+1, N):  # i의 오른쪽 인덱스 j
            if arr[i] > arr[j]:
                cnt += 1
        # cnt 중 최대값
        if maxV < cnt:
            maxV = cnt
    print(f'#{tc} {maxV}')