N = int(input())
cup = [list(map(int, input().split())) for _ in range(N)]

ball = 1

for i in range(N):
    if cup[i][0] == ball:
        ball = cup[i][1]
    elif cup[i][1] == ball:
        ball = cup[i][0]

print(ball)