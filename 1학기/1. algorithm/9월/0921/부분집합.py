arr = [3, 6, 7, 1, 5, 4]
n = len(arr)

for i in range(1, 1<<4):
    for j in range(n):
        if i & (1<<j):      # j번 비트가 0이 아니면 arr[j] = 부분집합의 원소
            print(j, end=' ')
    print()