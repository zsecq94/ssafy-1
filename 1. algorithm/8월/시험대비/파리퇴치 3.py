import sys
sys.stdin = open('123.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]


    maxV = 0
    for i in range(N-M):
        for j in range(N-M):
            sumV = 0
            for ii in range(M+1):
                for jj in range(M+1):
                    if ii == jj:
                        sumV += arr[i+ii][j+jj]
            print(sumV)
        print()