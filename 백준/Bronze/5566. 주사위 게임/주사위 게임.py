N, M = map(int, input().split())
board = [0]+[int(input()) for _ in range(N)]
dice = [0]+[int(input()) for _ in range(M)]
i = 1
for n in range(1, M+1):
    i += dice[n]
    if i >= N:
        print(n)
        break
    i += board[i]
    if i >= N:
        print(n)
        break