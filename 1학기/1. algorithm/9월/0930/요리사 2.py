import sys; sys.stdin = open('123.txt', 'r')

# def combi(k, s):
#     global minV
#     if k == N//2:
#         t = abs(calc(aList) - calc(bList))
#         if minV > t:
#             minV = t
#         return
#
#     for i in range(s, N-r+k):
#         aList[k] = i
#         combi(k+1, i+1)


def rec(k, aList, bList):
    global minV
    if k == N:
        if len(aList) == len(bList):
            t = abs(calc(aList) - calc(bList))
            if minV > t:
                minV = t
        return
    rec(k+1, aList+[k], bList)
    rec(k+1, aList, bList+[k])


def calc(arr):
    result = 0
    for i in arr:
        for j in arr:
            result += S[i][j]
    return result


for tc in range(1, int(input())+1):
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]

    aList = []
    bList = []
    minV = 999999999
    # 빈 리스트를 보내야 재귀를 돌릴 수 있음
    rec(0, [], [])
    print(f'#{tc} {minV}')