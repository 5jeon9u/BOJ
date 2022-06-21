val_lst = []

for i in range(0, 9):
    x = int(input())
    val_lst.append(x)

max_idx = 0
for j in range(0, len(val_lst)):
    if val_lst[max_idx] < val_lst[j]:
        max_idx = j
print(val_lst[max_idx])
print(max_idx + 1)