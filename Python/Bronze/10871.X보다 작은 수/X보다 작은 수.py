x, y= map(int,input().split())
a = list(map(int,input().split()))

for i in range(0, x):
    if a[i] < y:
        print(a[i], end = ' ')