'''
# 순열
N = 4
for i in range(N):
    for j in range(N):
        if j == i:
            continue
        for k in range(N):
            if k == i or k == j:
                continue
            for l in range(N):
                if l == i or l == j or l == k:
                    continue
                print(i, j, k, l)

def perm(k):
    if k == R:
        print(result)
        return
    for i in range(N):
        if visited[i] == True:
            continue
        visited[i] =  True
        result[k] = i
        perm(k+1)
        visited[i] = False

N = 5
R = 3
result = [-1] * R
visited = [False] * N
perm(0)
'''




'''
org = [3, 7, 9]
# 부분집합
for i in [0, 1]:
    for j in [0, 1]:
        for k in [0, 1]:
            print(i, j, k)
            if i == 1:
                print(org[0], end=' ')
            if j == 1:
                print(org[1], end=' ')
            if k == 1:
                print(org[2], end=' ')
            print()

def par(k):
    if k==N:
        print(result)
        for i in range(N):
            if result[i] == 1:
                print(org[i], end=' ')
        print()
        return

    for i in [0, 1]:
        result[k] = i
        par(k+1)

org = [3, 7, 9]
N = 3
result = [-1] * N
par(0)
'''



'''
# 조합

for i in range(0, N-R+1):
    for j in range(i+1, N-R+2):
        for k in range(j+1, N-R+3):
            print(i, j, k)

def comb(k, s):
    if k == R:
        print(result)
        return

    for i in range(s, N-(R-k)+1):
        result[k] = i
        comb(k+1, i+1)

N = 5
R = 3
result = [-1] * R
comb(0, 0)
'''