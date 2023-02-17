import sys; sys.stdin = open('123.txt', 'r')

# 16진수를 입력 받아 2진수로 바꾸기
def asd(i):
    # 들어온 문자가 숫자면 숫자형으로 바꿔서 추가
    if i.isdecimal():
        intV = int(i)
    # 아니면 아스키코드로 계산 A:10, B:11, C:12, D:13, E:14, F:15 + 10
    else:
        intV = ord(i) - ord('A') + 10

    result = ''
    # 바꾼 숫자를 2진수로 변환
    for i in range(4):
        # 8과 &(AND)연산 연산 후 왼쪽으로 1 시프트[ex)바꾼 숫자가 15면 1111 & 1000]
        if intV & 8:
            result += '1'
        else:
            result += '0'
        intV <<= 1

    return result

T = int(input())
for tc in range(1, T+1):
    arr = input().split()
    a = int(arr[0])
    b = arr[1]

    result1 = ''
    for i in b:
        result1 += asd(i)

    print(f'#{tc} {result1}')