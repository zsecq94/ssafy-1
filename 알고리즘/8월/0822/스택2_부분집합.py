
def f(i, N):
    if i == N:
        for i in range(N):
            if bit[i]:
                print(A[i], end= ' ')
        print()
    else:
        bit[i] = 1


        f(i+1, N)
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0] * 10
f(0, 10)