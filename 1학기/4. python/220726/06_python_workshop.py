# 1.
list_a = []
def duplicated_letters(a):
    for i in a:
        if a.count(i) > 1:
            if i not in list_a:
                list_a.append(i)
    return list_a
    
# print(duplicated_letters('apple'))
# print(duplicated_letters('banana'))

# 2.
list_a = []
def low_and_up(a):
    count = 0
    for i in a:
        if count % 2 == 0:
            list_a.append(i)
            count += 1
        elif count % 2 == 1:
            t = i.upper()
            list_a.append(t)
            count += 1
    return ''.join(list_a)
# print(low_and_up('apple'))

# 3.
def lonely(a):
    list_a = [a[0]]
    for i in a:
        if list_a[-1] != i:
            list_a.append(i)
    return list_a
                
a = [1, 1, 3, 3, 0, 1, 1]
# print(lonely(a))
