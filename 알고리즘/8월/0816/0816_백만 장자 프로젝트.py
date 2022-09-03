import sys
sys.stdin = open('123.txt', 'r')


def my_max(arr):
    maxV = 0
    for i in range(N):
        if maxV < arr[i]:
            maxV = arr[i]
            maxP = i
    return maxV, maxP

def my_sum(arr):
    sumV = 0
    cnt = 0
    for j in range(len(arr)):
        sumV += arr[j]
        cnt += 1
    return sumV, cnt




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    while:
    maxV, maxP = my_max(arr)
    print(my_sum(arr[:maxP]))
