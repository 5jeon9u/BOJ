import sys
N = int(sys.stdin.readline())
stack = []
total = 0
for i in range(N):
    num = int(sys.stdin.readline())
    if num != 0:
        total += num
        stack.append(num)
    elif num == 0:
        x = stack.pop()
        total -= x
print(total)