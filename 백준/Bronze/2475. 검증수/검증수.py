lst = list(map(int, input().split()))

cnt = 0

for i in range(len(lst)):
    cnt += (lst[i]**2)

print(cnt%10)
