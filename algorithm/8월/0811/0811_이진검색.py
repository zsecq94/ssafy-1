def find(key):
    st = 0
    ed = N-1
    while st <= ed:
        m = (st+ed) // 2
        if lst[m] == key:
            return m
        elif lst[m] < key:
            st = m+1
        else:
            ed = m-1
    return -1

N = 6
lst = [2, 4, 7, 9, 11, 19]
print(find(2))
print(find(19))
print(find(7))
print(find(20))
print(find(1))
print(find(8))