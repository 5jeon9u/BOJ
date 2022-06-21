x = int(input())
lst = list(map(int, input().split()))
max = lst[0]
su = 0
co = 0

for i in range(x):
    if max < lst[i]:
        max = lst[i]

for j in range(x):
    lst[j] = lst[j]/max*100
    su += lst[j]
    co += 1

print(su/co)