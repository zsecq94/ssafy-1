import sys
sys.stdin = open('123.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input()))

    cnt = [0] * 10
    maxC = 0

    for i in range(N):
        cnt[arr[i]] += 1
        if maxC < cnt[arr[i]]:
            maxC = cnt[arr[i]]
    maxV = 0
    result = 0
    for j in range(len(cnt)):
        if maxV <= cnt[j]:
            maxV = cnt[j]
            if result < j:
                result = j
    print(f'#{tc} {result} {maxC}')