import sys; sys.stdin = open('123.txt', 'r')

def pwd(i):
    if i.isdecimal():
        intV = int(i)
    else:
        intV = ord(i) - ord('A') + 10

    save = ''
    for j in range(4):
        if intV & 8:
            save += '1'
        else:
            save += '0'
        intV <<= 1
    return save

def pat(j):
    pat = {
        '001101': '0', '010011': '1', '111011': '2', '110001': '3',
        '100011': '4', '110111': '5', '001011': '6', '111101': '7',
        '011001': '8', '101111': '9',
    }
    return pat[j]

def six(q):
    result1 = ''
    asd = q
    d = asd + 6
    while asd != d:
        result1 += result[asd]
        asd += 1
    result1 = result1[::-1]
    return result1

for tc in range(1, int(input())+1):
    num = input()
    result = ''
    for i in num:
        result += pwd(i)
    result = result[::-1]

    save = []
    for j in range(len(result)):
        if result[j] == '1':
            for q in range(j, len(result)-6, 6):
                save += [six(q)]
            break
    save = save[::-1]

    real_last = ''
    for last in save:
        real_last += pat(last)

    print(f'#{tc} {real_last}')


