A, B = map(int, input().split(' '))
C = int(input())

minute = B + C
new = 0

new += (minute % 60)
A += (minute // 60)

if A >= 24:
    A -= 24

print(A, new)