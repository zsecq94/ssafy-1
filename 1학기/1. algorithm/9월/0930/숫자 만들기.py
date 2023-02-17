import sys; sys.stdin = open('123.txt', 'r')
'''
+ - * /
'''
def bfs():
    q = []



for tc in range(1, int(input())+1):
    N = int(input())
    calc = list(map(int, input().split()))
    arr = list(map(int, input().split()))

