A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

if A < 0:
    sec = (C * (-A)) + D + (E * B)
elif A == 0:
    sec = D + (E * B)
elif A > 0:
    sec = E * (B - A)

print(sec)