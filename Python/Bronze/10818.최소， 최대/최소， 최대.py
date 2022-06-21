x = int(input())
y = list(map(int, input().split()))

max = y[0]
min = y[0]

for i in range(0, x):
    if max < y[i]:
        max = y[i]
    if min > y[i]:
        min = y[i]

print(min, max)
