import sys
N = int(sys.stdin.readline())
stack = []
T = -1
for i in range(N):
    lst = list(sys.stdin.readline().split())
    if lst[0] == 'push':
        stack.append(int(lst[1]))
        T += 1
    elif lst[0] == 'pop':
        if T == -1:
            print(-1)
        else:
            print(stack.pop())
            T -= 1
    elif lst[0] == 'size':
        print(T+1)
    elif lst[0] == 'empty':
        if T == -1:
            print(1)
        else:
            print(0)
    elif lst[0] == 'top':
        if T == -1:
            print(-1)
        else:
            print(stack[T])