import sys
sys.stdin = open('123.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    MID = N//2
    st = ed = MID
    sumV = 0
    for row in range(N):
        for col in range(st, ed+1):
            sumV += arr[row][col]
        if row <= MID:
            st -= 1
            ed += 1
        else:
            st += 1
            ed -= 1