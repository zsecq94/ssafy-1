N = int(input())
arr = [list(map(int, input().split()))for _ in range(N)]

s0 = 0
s1 = 0
s2 = 0
s3 = 0
s4 = 0
s5 = 0
for i in range(N):
    for j in range(N):
        if i + j == 1:
            s1 += arr[i][j]
        elif i + j == 0:
            s0 += arr[i][j]
        elif i + j == 2:
            s2 += arr[i][j]
        elif i + j == 3:
            s3 += arr[i][j]
        elif i + j == 4:
            s4 += arr[i][j]
        elif i + j == 5:
            s5 += arr[i][j]
print(s0, s1, s2, s3, s4, s5)

'''
s = [0]*(2*N-1)
for i in range(N):
    for j in range(N):
        s[i+j] += arr[i][i]
print(s)
'''