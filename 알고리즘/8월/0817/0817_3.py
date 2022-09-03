
def factorial(n):   # # n! = n*(n-1)!
    if n == 1:
        return 1
    t = factorial(n-1)
    return n*t

for i in range(21):
    print(i, factorial(i))


'''

def fib(n):
    if n <= 1:
        return n

    t1 = fib(n-1)
    t2 = fib(n-2)
    return t1 + t2

print(fib(5))
'''