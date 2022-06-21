while True:
    lst = list(map(int, input().split()))

    count = 0
    width = 0

    count = lst[0] + lst[1] + lst[1]

    if count == 0:
        break

    for i in range(1, len(lst)):
        if lst[i-1] > lst[i]:
            lst[i], lst[i - 1] = lst[i-1], lst[i]


    if lst[0]**2 + lst[1]**2 == lst[2]**2:
        print('right')
    else:
        print('wrong')