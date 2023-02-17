import sys; sys.stdin = open('123.txt', 'r')

arr = [[0] * 500 for _ in range(500)]

sumX = 0
sumY = 0
minX = 501
minY = 501
N = int(input())
for _ in range(6):
    A, B = map(int, input().split())

    if A == 1:
        sumX += B
    if A == 3:
        sumY += B
    if A == 2:
        if minX > B:
            minX = B
    if A == 4:
        if minY > B:
            minY = B
maxV = sumX * sumY
minV = minX * minY
print(maxV - minV)


