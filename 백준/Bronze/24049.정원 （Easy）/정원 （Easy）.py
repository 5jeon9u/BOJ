N, M = map(int, input().split()) # 행,열

r = list(map(int, input().split())) # 행의 시작
c = list(map(int, input().split())) # 열의 시작

flower = [[0] * (M+1) for _ in range(N+1)]

for i in range(1, len(r)+1):
    flower[i][0] = r[i-1]

for j in range(1, len(c)+1):
    flower[0][j] = c[j-1]

for m in range(1, N+1):
    for n in range(1, M+1):
        if flower[m][n-1] == flower[m-1][n]:
            flower[m][n] = 0
        else:
            flower[m][n] = 1

print(flower[N][M])