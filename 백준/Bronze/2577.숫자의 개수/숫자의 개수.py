x = int(input())
y = int(input())
z = int(input())

num = list(str(x * y * z))

for i in range(10):
    print(num.count(str(i)))