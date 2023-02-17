import sys; sys.stdin = open('123.txt', 'r')

def merge(lLst, rLst):
    global cnt
    lp = rp = 0
    result = []
    while lp < len(lLst) and rp < len(rLst):
        if lLst[lp] < rLst[rp]:
            result.append(lLst[lp])
            lp += 1
        else:
            result.append(rLst[rp])
            rp += 1

    if lLst[-1] > rLst[-1]:
        cnt += 1
    result.extend(lLst[lp:])
    result.extend(rLst[rp:])
    return result


def merge_s(lst):
    if len(lst) == 1:
        return lst
    mid = len(lst) // 2
    left = merge_s(lst[:mid])
    right = merge_s(lst[mid:])
    return merge(left, right)

for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0

    result = merge_s(arr)
    print(f'#{tc} {result[N//2]} {cnt}')
