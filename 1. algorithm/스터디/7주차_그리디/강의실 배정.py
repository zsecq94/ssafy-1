import sys; sys.stdin = open('123.txt', 'r')

N = int(input())

result = [[-1, -1] for _ in range(N)]
for i in range(N):
    a, b = map(int, input().split())
    for j in range(N):
        if a >= result[j][1]:
            result[j][0] = a
            result[j][1] = b
            break
cnt = 0
for i in result:
    if sum(i) >= 0:
        cnt += 1

print(cnt)
