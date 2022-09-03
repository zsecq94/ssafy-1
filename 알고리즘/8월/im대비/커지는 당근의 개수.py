import sys; sys.stdin = open('123.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split())) + [0]

    maxV = 0
    cnt = 1
    for i in range(N-1):
        if arr[i] < arr[i+1]:
                cnt += 1
                if maxV < cnt:
                    maxV = cnt
        else:
            if maxV < cnt:
                maxV = cnt
            cnt = 1
    print(maxV)
