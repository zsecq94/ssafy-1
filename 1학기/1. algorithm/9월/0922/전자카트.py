# import sys; sys.stdin = open('123.txt', 'r')

def perm(k, midSum, s):
    global minV
    # 포문을 다 돌고나면 최소값 계산
    if k == N:
        midSum += arr[s][0]
        minV = min(minV, midSum)
        return

    for i in range(N):
        if visited[i]:
            continue
        visited[i] = True
        perm(k+1, midSum+arr[s][i], i)
        visited[i] = False


for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 방문 순서를 만들기 위해
    visited = [False] * N
    # 0에서 출발하기 때문에 미리 처리(1에 먼저 방문해야 함, 0은 마지막에)
    visited[0] = True
    # 100이하의 자연수만 입력받음
    minV = 101 * N
    # 값을 저장하기 위해
    midSum = 0
    # (시작점, 중간 값, 좌표)
    perm(1, 0, 0)
    print(f'#{tc} {minV}')