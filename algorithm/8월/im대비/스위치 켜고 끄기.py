import sys; sys.stdin = open('123.txt', 'r')

N = int(input())
arr = [-1] + list(map(int, input().split()))
s = int(input())
for _ in range(s):
    number = list(map(int, input().split()))

    if number[0] == 1:
        for i in range(number[1], len(arr), number[1]):
            if arr[i] == 1:
                arr[i] = 0
            else:
                arr[i] = 1
    elif number[0] == 2:
        idx = number[1]
        for i in range(idx, idx+1):
            z = 1
            while arr[i-z] >= 0 and arr[i+z] <= len(arr) and arr[i-z] == arr[i+z]:
                if arr[i-z] == 1:
                    arr[i-z] = 0
                elif arr[i-z] == 0:
                    arr[i-z] = 1
                if arr[i+z] == 1:
                    arr[i+z] = 0
                elif arr[i+z] == 0:
                    arr[i+z] = 1
                z += 1
            if arr[i] == 1:
                arr[i] = 0
            else:
                arr[i] = 1

for i in range(1, N, 20):
    print(*arr[i: 20 + i])