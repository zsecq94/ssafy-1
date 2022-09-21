# import sys; sys.stdin = open('123.txt', 'r')

def f(x, y, a):
    global cntA, cntB, cntC
    check = arr[x][y]
    for i in range(x, x+a):
        for j in range(y, y+a):
            if check != arr[i][j]:
                for n in range(3):
                    for m in range(3):
                        # 이 문제의 핵심
                        f(x+n*a//3, y+m*a//3, a//3)
                return
    # for문을 다 돌아도 check와 다른게 없다면 추가 or check와 다른게 나올때 마다 추가
    if check == -1:
        cntA += 1
    elif check == 0:
        cntB += 1
    else:
        cntC += 1


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cntA = 0
cntB = 0
cntC = 0
# 위치 계산을 위해 x, y, N을 보냄
f(0, 0, N)
print(cntA)
print(cntB)
print(cntC)