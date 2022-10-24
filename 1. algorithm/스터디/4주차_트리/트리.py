import sys; sys.stdin = open('123.txt', 'r')

def dfs(v):
    arr[v] = 99
    for i in range(len(arr)):
        if v == arr[i]:
            dfs(i)

N = int(input())
arr = list(map(int, input().split()))
D = int(input())

dfs(D)
cnt = 0
for i in range(len(arr)):
    if arr[i] != 99 and i not in arr:
        cnt += 1
print(cnt)