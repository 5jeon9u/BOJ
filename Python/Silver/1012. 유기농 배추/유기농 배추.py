T = int(input())

for tc in range(1, T+1):
    M, N, K = map(int, input().split()) # 가로, 세로, 배추 갯수
    farm = [[0]*M for _ in range(N)] # 배추밭

    # 배추 심기
    for i in range(K):
        a, b = map(int, input().split())
        farm[b][a] = 1

    
    # 방문 확인 배열
    visit = [[0] * M for _ in range(N)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    cnt = 0 # 필요한 배추의 개수
    Q = [] # 큐 생성

    for m in range(N):
        for n in range(M):
            # 아직 방문하지 않은 배추
            if visit[m][n] == 0 and farm[m][n] == 1:
                cnt += 1
                visit[m][n] = cnt # 방문 체크
                Q.append((m, n))

                while Q:
                    x, y = Q.pop(0)

                    for k in range(4):
                        ni = x + dr[k]
                        nj = y + dc[k]
                        # 주위에 방문안한 배추가 있을 경우
                        if (0 <= ni < N) and (0 <= nj < M) and (visit[ni][nj] == 0) and (farm[ni][nj] == 1):
                            # 방문 진행
                            visit[ni][nj] = cnt
                            Q.append((ni, nj))
                        else:
                            continue

    print(cnt)