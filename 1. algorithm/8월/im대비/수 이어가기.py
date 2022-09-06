import sys; sys.stdin = open('123.txt', 'r')

N = int(input())

result = []
for i in range(N//2, N+1):
    st = [N]
    st.append(i)
    a = 0
    while True:
        if st[a] - st[a+1] >= 0:
            st.append(st[a] - st[a+1])
            a += 1
        else:
            break
    if len(result) < len(st):
        result = st

print(len(result))
print(' '.join(map(str, result)))