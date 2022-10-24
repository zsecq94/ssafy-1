import sys; sys.stdin = open('123.txt', 'r')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def asd(x, y):
    global cntV
    cnt = 1                     # 시작점을 2로 채우고 카운트를 1 올리고 시작
    arr[x][y] = 2
    st = []                     # 빈 스택을 만들고
    st.append((x, y))           # 초기 좌표를 저장
    while st:                   # 스택에 좌표가 있는동안 반복
        ii, jj = st.pop(0)      # 스택에 저장되어있는 좌표를 ii, jj에 할당
        for i in range(4):      # 델타로 탐색
            ni = ii + dr[i]
            nj = jj + dc[i]
            if 0 <= ni < m and 0 <= nj < n:
                if arr[ni][nj] == 0:        # 탐색한 곳의 데이터가 0이면
                    st.append((ni, nj))     # 스택에 좌표를 저장하고
                    arr[ni][nj] = 2         # 2로 바꾸고 cnt += 1
                    cnt += 1
    cntV += 1       # 빠져나갈 때 한구역 끝이므로 cntV에 += 1
    return cnt

m, n, k = map(int, input().split())
arr = [[0] * n for _ in range(m)]

for _ in range(k):
    a = list(map(int, input().split()))

    # 입력받은 구역 1로 채우는 작업
    for i in range(a[1], a[3]):
        for j in range(a[0], a[2]):
            if arr[i][j] == 0:
                arr[i][j] = 1

cnt1 = []
cntV = 0
# 0인 구역을 찾아 asd함수로 넘김
for i in range(m):
    for j in range(n):
        if arr[i][j] == 0:
            x, y = i, j
            cnt1.append(asd(x, y))          # 리턴받은 cnt를 cnt1에 저장
result = ' '.join(map(str, sorted(cnt1)))   # 정렬
print(cntV)
print(result)

