# key를 입력받아 lst 에서 일치하는 경우 위치를 return한다.
# 없는 경우에는 return -1

def find(key):
    pos = 0
    while pos < N:
        if lst[pos] == key:
            return pos
        pos += 1
    return -1

def find1(key):
    pos = 0
    while pos < N and lst[pos] < key:
        pos += 1
    if pos<N and lst[pos] == key:
        return pos

    return -1

N = 7
# lst = [4, 9, 11, 23, 2, 19, 7]
# print(find(4))
# print(find(7))
# print(find(9))
# print(find(20))

lst = [1, 4, 9, 11, 17, 19, 23]
print(find1(4))
print(find1(17))
print(find1(9))
print(find1(23))
print(find1(98))