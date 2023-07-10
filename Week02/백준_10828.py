# 스택
import sys
input = sys.stdin.readline
N = int(input())
stack = []
for _ in range(N):
    input_list = list(map(str, input().split()))
    order = input_list[0]
    if len(input_list) == 2:
        num = int(input_list[1])
    if order == 'push':
        stack.append(num)
    elif order == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif order == 'size':
        print(len(stack))
    elif order == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif order == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
