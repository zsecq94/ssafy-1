import sys
sys.stdin = open('123.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))

    cnt = [0] * len(Ai)
    for i in range(len(Ai)):
        for j in range(len(Bj)):
            if len(Bj) == 0:
                break
            elif Bj[j] >= Ai[i]:
                cnt[i] += 1
                Bj[j] = 0
    result = cnt.index(max(cnt)) + 1
    print(f'#{tc} {result}')
