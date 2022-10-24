import sys; sys.stdin = open('123.txt', 'r')

N = int(input())
arr = list(map(int, input().split()))
maxV = 0
sumV = 0
for i in range(len(arr)):
    if arr[i] >= 0:
        sumV += arr[i]
    elif arr[i] < 0:
        if maxV < sumV:
            maxV = sumV
        sumV = 0
print(maxV)