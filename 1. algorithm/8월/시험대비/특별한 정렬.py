import sys
sys.stdin = open('123.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = sorted(list(map(int, input().split())))

    result = []
    maxV = N - 1
    minV = 0
    for i in range(5):
        result.append(arr[maxV])
        result.append(arr[minV])
        maxV -= 1
        minV += 1
        if maxV == N//2-1:
            break
    result = " ".join(map(str, result))
    print(f'#{tc} {result}')