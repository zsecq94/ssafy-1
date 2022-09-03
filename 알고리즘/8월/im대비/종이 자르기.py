import sys; sys.stdin = open('123.txt', 'r')

x, y = map(int, input().split())
arr = [[0] * y for _ in range(x)]

N = int(input())

maxX = 101
maxY = 0
for i in range(N):
    sumX = 0
    sumY = 0
    A, B = map(int, input().split())

    if A == 0:
        sumX = y - B
        if maxX > sumX:
            maxX = sumX
    else:
        sumY = x - B
        if maxY < sumY:
            maxY = sumY
print(maxX * maxY)
