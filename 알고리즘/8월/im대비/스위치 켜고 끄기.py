import sys; sys.stdin = open('123.txt', 'r')

N = int(input())
arr = [-1] + list(map(int, input().split()))
S = int(input())

for _ in range(S):
    A, num = map(int, input().split())
    if A == 1:
        for i in range(num, N+1, num):
            if arr[i] == 1:
                arr[i] = 0
            else:
                arr[i] = 1
    else:
        if arr[num] == 1:
            arr[num] = 0
        else:
            arr[num] = 1
        z = 1
        while num-z > 0 and num+z <= N and arr[num-z] == arr[num+z]:
            if arr[num-z] == 1:
                arr[num-z] = 0
                arr[num+z] = 0
            else:
                arr[num-z] = 1
                arr[num+z] = 1
            z += 1

for i in range(1, N+1):
    print(arr[i], end=" ")
    if i % 20 == 0:
        print()