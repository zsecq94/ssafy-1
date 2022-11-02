import sys; sys.stdin = open('123.txt', 'r')

def go(arr, result):
    cnt = 0
    arr1 = arr[:]
    for i in range(1, N):
        if arr1[i - 1] == result[i - 1]:
            continue
        for j in range(i - 1, i + 2):
            if j < N:
                arr1[j] = 1 - arr1[j]
        cnt += 1

    if arr1 == result:
        return cnt
    else:
        return -3


N = int(input())
arr = list(map(int, input()))
result = list(map(int, input()))

cntV = []

cntV.append(go(arr, result))
arr[0] = 1 - arr[0]
arr[1] = 1 - arr[1]
cntV.append(go(arr, result)+1)

resultV = 999999999
for i in cntV:
    if resultV > i and i >= 0:
        resultV = i

if resultV == 999999999:
    print(-1)
else:
    print(resultV)