x = int(input())

count = 0
c = x
num = 0
num1 = 0

while True:
    num = c % 10
    num1 = c // 10
    c = (num * 10) + ((num + num1) % 10)
    count += 1

    if(x == c):
        break

print(count)