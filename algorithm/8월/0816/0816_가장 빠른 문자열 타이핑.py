import sys
sys.stdin = open('123.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    A, B = list(input().split())
    C = len(B)

    cnt = 0
    D = 0
    while len(A) > D:
        if A[D:D+len(B)] == B:
            cnt += 1
            D += len(B)
        else:
            cnt += 1
            D += 1
    print(f'#{tc} {cnt}')