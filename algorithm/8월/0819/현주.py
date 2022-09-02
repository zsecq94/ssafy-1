import sys
sys.stdin = open('123.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    cnt = [0] * (N+1)
    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for j in range(L, R+1):
            cnt[j] = i
    result = ' '.join(map(str, cnt[1:]))
    print(f'#{tc} {result}')