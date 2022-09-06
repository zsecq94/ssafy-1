import random

is_playing = True

while is_playing:
    print('================================')
    print('        Up and Down Game        ')
    print('================================')

    answer = random.randint(1, 10000)  # 1이상 10000이하의 난수
    counts = 0  # 몇 번만에 정답을 맞혔는지 담는 변수
    print(answer)

    # 여기부터 코드를 작성하세요.
    # 1. 숫자입력받기 : 범위 안의 숫자가 입력될 때까지 반복
    while True:
        inputStr = input('1이상 10000이하의 숫자를 입력하세요. : ')
        counts += 1
        if not inputStr.isdecimal or int(inputStr) < 1 or int(inputStr) > 10000:
            continue
        
        # print(inputStr)
        num = int(inputStr)
        if num > answer:
            print('Down!!')
            continue
        elif num < answer:
            print('Up!!')
            continue
        # else:

        print(f'Correct!!! {counts}회 만에 정답을 맞히셨습니다.')
        break

    retry = '-'
    print('게임을 재시작 하시려면 y, 종료하시려면 n을 입력하세요.')
    while retry != 'y':
        if retry == 'y':
            break
        elif retry == 'n':
            print('이용해주셔서 감사합니다. 게임을 종료합니다.')
            is_playing = False
            break

        retry = input()