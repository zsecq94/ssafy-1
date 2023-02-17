a = 97

for j in range(7, -1, -1):
    print(a&(1<<j))
    #     print('1')
    # else:
    #     print('0')

for i in range(4):
    if a&8:
        a = a*2