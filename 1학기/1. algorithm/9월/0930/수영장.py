import sys; sys.stdin = open('123.txt', 'r')

def rec(k, mid):
    global minV
    if k >= 12:
        if minV > mid:
            minV = mid
        return

    rec(k+1, mid+min(N[0]*arr[k], N[1]))
    rec(k+3, mid+N[2])


for tc in range(1, int(input())+1):
    N = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    minV = 9999999999999999999999999999
    rec(0, 0)

    if minV > N[3]:
        minV = N[3]
    print(f'#{tc} {minV}')
