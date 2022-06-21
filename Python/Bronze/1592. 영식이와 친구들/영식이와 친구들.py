N, M, L = map(int, input().split())

lst = [0] * (N) # 공을 받은 횟수 저장
cnt = 0 # 총 공을 던진 횟수
i = 0

while i <= N:
    lst[i] += 1
    if lst[i] == M: # 현재 공을 받은 사람의 받은 횟수가 M일 경우, 게임이 종료
        print(cnt)
        break
    elif lst[i] % 2 == 1: # 공을 받은 횟수가 홀수일 경우
        i = (i + L) % N # 시계 방향으로 L번째 있는 사람에게 공을 던지므로
    elif lst[i] % 2 == 0:
        i = (i+(N-L))%N
    cnt += 1