N = 10
result = []
for j in range(N):
    check = 1<<j
    if N & check:
        result.append(N[j])
print(result)