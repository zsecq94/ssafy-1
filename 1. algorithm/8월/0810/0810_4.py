numR = 5
numC = 5
sumV = 0
ARR = [list(map(int, input().split())) for _ in range(numR)]
for curR in range(numR):
    for curC in range(numC):
        for d in range(4):
            newC = curC + 