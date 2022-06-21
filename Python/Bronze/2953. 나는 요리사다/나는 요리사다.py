max_total = 0
who = 0

for i in range(1, 6):
    matrix = list(map(int, input().split()))
    total = 0
    for j in range(4):
        total += matrix[j]

    if max_total < total:
        max_total = total
        who = i


print(who, max_total)