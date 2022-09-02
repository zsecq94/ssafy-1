import sys; sys.stdin = open('123.txt', 'r')

def hwa(Z):
    q = []
    M = N
    result = []
    while Z:
        q.append(Z.pop(0))
        q.append(Z.pop(1))
        while len(q) != 1:
            q[0][1] //= 2
            if len(Z) == 1:
                result.append(q)
                return Z
            elif q[0][1] == 0:
                result.append(q.pop(0))
                M += 1
            else:
                q.append(q.pop(0))

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    Z = []
    for i in range(M):
        Z.append([i, arr[i]])

    hwa(Z)
    maxV = 0
    for i in range(M):
        if maxV < Z[0][i][1]:
            maxV = Z[0][i][0]
    print(f'#{tc} {maxV+1}')