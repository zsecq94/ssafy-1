import sys; sys.stdin = open('123.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    area = list(map(int, input().split()))
    arr = []
    for i in range(0, len(area), 2):
        arr.append([area[i], area[i+1]])

