import sys
sys.stdin = open('123.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = list(range(1, 13))

    count = 0
    for i in range(1<<len(A)):
        result = []
        sumV = 0

        for j in range(len(A)):
            chk = 1<<j
            if i & chk:
                result.append(j+1)
                sumV += j+1
        if sumV == K and len(result) == N:
            count += 1

    print(f"#{tc} {count}")