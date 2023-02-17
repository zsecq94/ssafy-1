import sys; sys.stdin = open('123.txt', 'r')

c, r = map(int, input().split())
k = int(input())

arr = [[0] * c for _ in range(r)]

# 번호표 순서가 범위를 넘어가면 0
if k > c*r:
    print(0)
    exit()

# 경로를 핸들링 할 좌표
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
hand = 0
x, y = 0, 0

for i in range(1, k+1):
    if i == k:
        print(y+1, x+1)

    # 좌표에 값을 넣고 시작
    else:
        arr[x][y] = i
        x += dx[hand]
        y += dy[hand]
        if x == r or y == c or x < 0 or y < 0 or arr[x][y] != 0:
            x -= dx[hand]
            y -= dy[hand]
            hand = ((hand+1) % 4)
            x += dx[hand]
            y += dy[hand]










