N = int(input()) # 숫자의 개수 N
num = int(input())

count = 0

for i in range(0, N):
    count += num % 10
    num //= 10

print(count)