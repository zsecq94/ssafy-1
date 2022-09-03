'''
N, M = map(int, input().split())
arr = [list(map(int, input().split()))for _ in range(N)]

# 행 우선 순회
for i in range(N): # 행의 좌표
    for j in range(M): # 열의 좌표
        arr[i][j + (M-1-2*j) * (i%2)] # 짝수일때 j빼고 날라감
    print(arr)


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N = 3
M = 4
arr = [[1, 2, 3, 4],[5, 6, 7, 8]]
for i in range(N):
    for j in range(M):
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N: # 유효한 인덱스면
                print(ni, nj)

numR = 2
numC = 3
ARR = [[1, 2, 3], [4, 5, 6]]

# 모든 row에 대해서
for row in range(numR):
    sumV = 0
    for idx in range(numC):
        sumV += ARR[row][idx]
    print(sumV)


ARR = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
print(ARR[1][1])
# 상
ARR[0][1] -1, +0

# 하
ARR[2][1] +1, +0

# 좌
ARR[1][0] +0, +0

# 우
ARR[1][2] +0, +1

curX = 1
curY = 1
ARR[curY][curX]


arr = [7, 2, 5, 3, 4, 6]
N = len(arr)

for i in range(N-1):
    minIdx = i  # 구간의 맨 앞을 최소값으로 가정
    for j in range(i+1, N):  # 실제 최소값 인덱스 찾기
        if arr[minIdx] > arr[j]:
            minIdx = j
    arr[minIdx], arr[i] = arr[i], arr[minIdx]  # 최소값을 구간 맨 앞으로

print(arr)
'''

