T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))

    maxV = 0
    cnt = 0
    for i in range(N):
        for j in range(len(arr)):
            if arr[j] == 1:
                cnt += 1
                if maxV < cnt:
                    maxV = cnt
            else:
                cnt = 0
    print(maxV)