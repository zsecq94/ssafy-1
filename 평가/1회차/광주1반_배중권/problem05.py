# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def check_password_length(password):
    if len(password) < 33:
        if len(password) >= 8:
            return True
        else:
            return False
    else:
        return False


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    password = 'q1w2e3r4'
    print(check_password_length(password)) # True
