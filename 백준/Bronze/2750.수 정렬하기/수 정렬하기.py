N = int(input())
lst = []

for i in range(0, N):
    a = int(input())
    lst.append(a)

for j in range(len(lst)-1, 0, -1):
    for k in range(0, j):
        if lst[k] > lst[k+1]:
            lst[k], lst[k+1] = lst[k+1], lst[k]

for m in range(0, len(lst)):
    print(lst[m])