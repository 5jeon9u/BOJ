import sys

N = int(sys.stdin.readline())
L = []

for i in range(N):
    L.append(sys.stdin.readline())

def score(OX):
    cnt = 1
    point = 0
    for k in OX:
        if k == 'O':
            point += cnt
            cnt += 1
        else:
            cnt = 1
    return point

for h in L:
    print(score(h))