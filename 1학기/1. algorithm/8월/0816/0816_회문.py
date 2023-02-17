import sys
sys.stdin = open('123.txt', 'r')

# 벨류가 회문이면 트루 아니면 False
def ischeck(value):
    if value == value[::-1]:
        return True
    else:
        return False

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    list_a = ''
    for i in range(N):
        for j in range(N-M+1):
            if ischeck(arr[i][j:j+M]):
                list_a = arr[i][j:j+M]
                break

            t = ''
            for k in range(M):
                t += arr[j+k][i]
            if ischeck(t):
                list_a = t
                break

    print(f'#{tc} {list_a}')