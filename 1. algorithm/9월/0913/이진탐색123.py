# 찾은 경우 일차원 배열의 index를 return하고 못찾으면 -1을 return
def find(key):
    pos = 1
    while tree[pos]:
        if key == tree[pos]:
            return pos
        if key > tree[pos]:
            pos = pos * 2 + 1
        else:
            pos = pos * 2
    return -1

def ino(root):
    if tree[root]:
        ino(root*2)
        print(tree[root], end= ' ')
        ino(root*2+1)

def insert(v):
    pos = 1
    while tree[pos]:
        if v < tree[pos]:
            pos = pos * 2
        else:
            pos = pos * 2 + 1
    tree[pos] = v

lst = [9, 4, 12, 13, 17, 15, 3, 6]
tree = [0] * 100

print(tree)
for d in lst:
    insert(d)

print(tree)

# print(tree)
# ino(1)
# print()
# print(find(9))
# print(find(6))
# print(find(17))
# print(find(98))