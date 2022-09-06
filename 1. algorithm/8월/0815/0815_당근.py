import sys
sys.stdin = open('123.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    maxV = 0
    cnt = 1
    for i in range(N-1):
        for j in range(i+1, N):
            if arr[i] < arr[j]:
                cnt += 1
                if maxV < cnt:
                    maxV = cnt
                    break
                break
            else:
                cnt = 1
                if maxV < cnt:
                    maxV = cnt
                break

    print(f'#{tc} {maxV}')