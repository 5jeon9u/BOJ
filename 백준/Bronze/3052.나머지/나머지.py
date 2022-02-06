new_set = set()

for i in range(10):
    a = int(input())
    new_set.add(a % 42)

print(len(new_set))