import sys
x = int(sys.stdin.readline())

count = 0
for i in range(0, x):
    a, b = map(int, sys.stdin.readline().split())
    count = a + b
    print(count)