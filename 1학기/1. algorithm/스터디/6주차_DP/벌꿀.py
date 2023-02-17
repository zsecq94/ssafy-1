import sys; sys.stdin = open('123.txt', 'r')

def find_max(i, j):
    global result
    a = 1
    sumV = 0
    save = []
    while a != M+1:
        sumV += arr[i][j]
        save.append([arr[i][j], i, j])
        a += 1
        j += 1
        if sumV > C:
            save.pop(-1)
            sumV -= arr[i][j-1]
            break

    if sumV <= C:
        result.append(save)

for tc in range(1, int(input())+1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = []
    visited = [[False] * N for _ in range(N)]
    a = 0
    while a != 2:
        for i in range(N):
            for j in range(N-M+1):
                if visited[i][j] == False:
                    find_max(i, j)

        sumVVV = 0
        ans = []
        for i in result:
            sumVV = 0
            z = 0
            save = []
            while z != len(i):
                sumVV += i[z][0]
                save.append([i[z][1], i[z][2]])
                z += 1
            if sumVVV < sumVV:
                sumVVV = sumVV
                ans.append(save)

        ans = ans[-1]
        for x, y in ans:
            visited[x][y] = True
        a += 1
        print(visited)