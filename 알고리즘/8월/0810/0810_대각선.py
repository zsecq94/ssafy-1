N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

s = 0
for i in range(N):
    for j in range(N):
        if i == j:
            s += arr[i][j]
print(s)
d = 0
for i in range(N):
    d += arr[i][N-1-i]
print(d)
'''
# s1 = 0
# s2 = 0
# for i in range(N):
#     for j in range(N):
#         if i > j:
#             s1 += arr[i][j]
#         elif i < j:
#             s2 += arr[i][j]
# print(s1, s2)
'''