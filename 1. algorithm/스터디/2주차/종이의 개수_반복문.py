# import sys; sys.stdin = open('123.txt', 'r')
def find(arr):
    cntA = 0
    cntB = 0
    cntC = 0
    # 1. 종이가 모두 하나의 숫자로 이루어 졌을때
    for i in range(N):
        for j in range(N):
            if arr[i][j] == -1:
                cntA += 1
            elif arr[i][j] == 0:
                cntB += 1
            else:
                cntC += 1

    resultA = 0
    resultB = 0
    resultC = 0
    if cntA == N * N:
        resultA += 1
    elif cntB == N * N:
        resultB += 1
    elif cntC == N * N:
        resultC += 1

    if resultA > 0 or resultB > 0 or resultC > 0:
        return resultA, resultB, resultC

    # (1)이 아닐때
    for q in range(0, N - 2, 3):
        for w in range(0, N - 2, 3):
            cntAA = 0
            cntBB = 0
            cntCC = 0
            for x in range(q, q + 3):
                for y in range(w, w + 3):
                    if arr[x][y] == -1:
                        cntAA += 1
                    elif arr[x][y] == 0:
                        cntBB += 1
                    else:
                        cntCC += 1
            if cntAA == 9:
                resultA += 1
            if 0 < cntAA < 9:
                resultA += cntAA
            if cntBB == 9:
                resultB += 1
            if 0 < cntBB < 9:
                resultB += cntBB
            if cntCC == 9:
                resultC += 1
            if 0 < cntCC < 9:
                resultC += cntCC
    return resultA, resultB, resultC

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

a = find(arr)
for i in a:
    print(i)