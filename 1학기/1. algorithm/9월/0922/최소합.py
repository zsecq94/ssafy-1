import sys; sys.stdin = open('123.txt', 'r')

def asd(r, c, midSum):
    global minV
    if r == N-1 and c == N-1:
        if minV > midSum:
            minV = midSum
        return

    if minV < midSum:
        return

    if r+1 < N:
        asd(r+1, c, midSum+arr[r+1][c])

    if c+1 < N:
        asd(r, c+1, midSum+arr[r][c+1])


for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    minV = 99999
    midSum = arr[0][0]
    asd(0, 0, midSum)
    print(f'#{tc} {minV}')