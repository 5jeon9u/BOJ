N = int(input())
for i in range(N):
    stack = []
    top = -1
    total = 'YES'
    lst = list(input())
    for j in range(len(lst)):
        if lst[j] == '(':
            stack.append(lst[j])
            top += 1
        elif lst[j] == ')':
            if top < 0:
                total = 'NO'
                break
            else:
                x = stack.pop()
                top -= 1
                if x == '(':
                    continue
                else:
                    total = 'NO'
                    break
    if top != -1:
        total = 'NO'
    print(total)