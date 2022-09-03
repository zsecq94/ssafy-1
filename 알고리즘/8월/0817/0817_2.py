'''
size = 100
st = [' '] * size
top = -1

def isEmpty():
    if top > 0:
        return False
    return True

def isFull():
    if top == size-1:
        return True
    return False

def push(item):
    global top
    if not isFull():
        top += 1
        st[top] = item
        print(st)
    else:
        print('overflow')

def peek():
    return st[top]

def pop():  # 팝 할때 사이즈 있는지 확인 필수
    global top
    if not isEmpty():
        item = st[top]
        top -= 1
        print(st)
        return item
    else:
        print('underflow')
        
push('A')
push('B')
push('C')
result = pop()
print(result)
print(pop())
print(pop())
print(pop())
'''

st = []

def push(item):
    st.append(item)
    
def isEmpty():
    if len(st) == 0:
        return True
    return False
    
def pop():  # isEmpty 대신 pop사용
    if not isEmpty():
        st.pop()