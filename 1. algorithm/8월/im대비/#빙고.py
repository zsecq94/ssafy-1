import sys; sys.stdin = open('123.txt', 'r')

def find(z):
    global cnt
    global bingo

    for r in range(5):
        for c in range(5):
            # 넘어온 값이랑 빙고판의 숫자가 같으면 빙고판의 숫자를 -1로 바꾸고 카운트를 1 추가
            if z == bg[r][c]:
                bg[r][c] = 'X'
                cnt += 1

                sumQ = 0
                sumP = 0
                # 빙고판의 숫자를 -1로 바꿨을때 빙고 구하기
                for ii in range(5):
                    sumR = 0
                    sumC = 0
                    # 역 대각 구하기
                    if bg[ii][len(arr)-ii-1] == 'X':
                        sumP += 1
                        if sumP == 5:
                            bingo += 1
                    for jj in range(5):
                        # 가로 구하기
                        if bg[ii][jj] == 'X':
                            sumR += 1
                            if sumR == 5:
                                bingo += 1
                        # 세로 구하기
                        if bg[jj][ii] == 'X':
                            sumC += 1
                            if sumC == 5:
                                bingo += 1
                        # 대각 구하기
                        if bg[ii] == bg[jj]:
                            if bg[ii][jj] == 'X':
                                sumQ += 1
                                if sumQ == 5:
                                    bingo += 1

bg = [list(map(int, input().split())) for _ in range(5)]
arr = [list(map(int, input().split())) for _ in range(5)]

result = []
cnt = 0
bingo = 0
# 사회자 숫자 구해서 넘기기
for i in range(5):
    for j in range(5):
        z = arr[i][j]
        find(z)
        # 빙고가 3보다 작으면 빙고는 0으로 초기화
        if bingo < 3:
            bingo = 0
        # 빙고가 3이상이면 result에 붙임
        if bingo >= 3:
            result.append(cnt)

print(result[0])