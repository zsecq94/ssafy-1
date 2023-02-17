import sys; sys.stdin = open('123.txt', 'r')

def perm(arr, n):
    result = []
    if n > len(arr):
        return result
    if n == 1:
        for i in arr:
            result.append([i])
    elif n > 1:
        for i in range(len(arr)):
            ans = [i for i in arr]
            ans.remove(arr[i])
            for p in perm(ans, n-1):
                result.append([arr[i]]+p)

    return result

arr = list(input())
result = []
for i in perm(arr, len(arr)):
    V = ''.join(i)
    C = V[::-1]
    if V == C:
        result.append(V)

result.sort()
if result:
    print(result[0])
else:
    print("I'm Sorry Hansoo")