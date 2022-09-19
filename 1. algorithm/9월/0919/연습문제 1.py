'''
10진수 : 0~9
    567 : 5*10^2 + 6*10^1 + 7*10^0
    0.123 : 1*10^-1 + 2*10^-2 + 3*10^-3
2진수 : 0~1
    1010 => 10진수 => 2진수
    1*2^3 + 0*2^2 + 1*2^1 + 0*2^0
    10진수 => 2진수
    1010 => 2로 나눈 나머지 : 2^0 => 0
    101 => 2로 나눈 나머지 : 2^1 => 1
16진수 : 0~9, A(10)~F(15)
    4A7 => 10진수
    4*16^2 + A(10)*16^1 + 2*16^0
    10진수 => 16진수
    16으로 계속 나누면 된다.

    2진수 => 16진수 1111(15)=F => 10000(0x10)
    1001 1111 0101 => 0x 9F5
8진수 : 0~7
'''

# a-문자열 이진수를 숫자 10진수로 만들어 return
def btod(s):
    result = 0
    for c in s:
        # result = result * 2 + int(c)
        result = (result << 1) | int(c)
    return result

# 문자열 16진수를 2진수 문자열로 만들어 return
def htob(c):
    # 16진수를 10진수로 바꾼 후 2진수로 만드든것이 일반적
    if c.isdecimal(): # 0~9까지의 숫자면
        intC = int(c)
    else:   # A=>10, B=>11, f=>15
        intC = ord(c) - ord('A') + 10

    result = ''
    for i in range(4):
        result = str(intC%2) + result
        intC //= 2

    # for i in range(4):
    #     if intC&8:
    #         result = '1' + result
    #     else:
    #         result = '0' + result
    #     intC *= 2

    return result

def patt():
    pat = {
        '0': '0000',
        '1': '0001',
        ...
    }
# a = '0000000111100000011000000111100110000110000111100111100111111001100111'
# # a = '00000010001101'
#
# for i in range(0, len(a), 7):
#     print(btod(a[i:i+7]))


b = '0F97A3'
#1 16진수 문자열을 이진수 문자열로
a = ''
for c in b:
    a = a + htob(c)

#2 2진수 문자열을 10진수 숫자로
for i in range(0, len(a), 7):
    print(btod(a[i:i+7]))