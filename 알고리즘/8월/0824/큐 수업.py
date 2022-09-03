n = 0
def deQ():
    global n
    Q.pop(n)

Q = []

Q.append(1)
Q.append(2)
Q.append(3)
print(deQ(Q))
print(deQ(Q))
print(deQ(Q))
