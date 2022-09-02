# 유클리드 호제법
# 최대공약수
def getGcd(a,b):
    while b!=0:
        a, b = b, a%b

    return a

# 최소공배수
print(24*16//getGcd(24,16))