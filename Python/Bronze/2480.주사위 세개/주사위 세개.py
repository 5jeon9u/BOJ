lst = list(map(int, input().split()))

val = 0 # 상금

if lst[0] == lst[1] == lst[2]:
    val = 10000 + lst[0] * 1000
    print(val)
elif lst[0] == lst[1]:
    val = 1000 + lst[0] * 100
    print(val)
elif lst[0] == lst[2]:
    val = 1000 + lst[0] * 100
    print(val)
elif lst[1] == lst[2]:
    val = 1000 + lst[1] * 100
    print(val)
else:
    max = lst[0]
    for i in range(1, len(lst)):
        if max < lst[i]:
            max = lst[i]
    val = max * 100
    print(val)