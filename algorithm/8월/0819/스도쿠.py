import sys
sys.stdin = open('123.txt', 'r')

# 스도쿠가 만족하면 1 아니면 0
def asd(arr):
    for i in range(9):
        cnt = [0] * 9
        for j in range(9):
            cnt[arr[i][j]-1] += 1
            if cnt[arr[i][j]-1] != 1:
                return 0

        cnt = [0] * 9
        for k in range(9):
            cnt[arr[k][i]-1] += 1
            if cnt[arr[k][i]-1] != 1:
                return 0

        cnt = [0] * 9
        for p in range(9):
            cnt[arr1[i][p]-1] += 1
            if cnt[arr1[i][p]-1] != 1:
                return 0
    return 1

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    arr1 = []

    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            temp = []
            for i in range(3):
                for j in range(3):
                    temp.append(arr[r+i][c+j])
            arr1.append(temp)

    result = asd(arr)
    print(f'#{tc} {result}')