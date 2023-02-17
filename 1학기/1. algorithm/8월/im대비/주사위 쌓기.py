import sys; sys.stdin = open('123.txt', 'r')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

final = 0
gal = []
for gal1 in range(1, 7):
    gal.append(gal1)
    result = []
    maxV = []
    for i in arr:
        if gal[-1] == i[0]:
            gal.append(i[5])
            result.append(i[1])
            result.append(i[2])
            result.append(i[3])
            result.append(i[4])
        elif gal[-1] == i[1]:
            gal.append(i[3])
            result.append(i[0])
            result.append(i[2])
            result.append(i[4])
            result.append(i[5])
        elif gal[-1] == i[2]:
            gal.append(i[4])
            result.append(i[0])
            result.append(i[1])
            result.append(i[3])
            result.append(i[5])
        elif gal[-1] == i[3]:
            gal.append(i[1])
            result.append(i[0])
            result.append(i[2])
            result.append(i[4])
            result.append(i[5])
        elif gal[-1] == i[4]:
            gal.append(i[2])
            result.append(i[0])
            result.append(i[1])
            result.append(i[3])
            result.append(i[5])
        elif gal[-1] == i[5]:
            gal.append(i[0])
            result.append(i[1])
            result.append(i[2])
            result.append(i[3])
            result.append(i[4])
        maxV.append(max(result))
        result = []
    if final < sum(maxV):
        final = sum(maxV)
    gal = []
print(final)