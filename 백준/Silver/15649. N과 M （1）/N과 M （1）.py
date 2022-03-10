N, M = map(int, input().split())
visited = [False] * N  # 탐사 여부 check
out = []  # 출력 내용

lst = [0] * N
for i in range(1, N+1):
    lst[i-1] = i

def perm(k, m):
    if k == m: # 2개의 수만을 취함
        print(' '.join(map(str, out)))
        return
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = True
                out.append(i+1)
                perm(k+1, m)
                visited[i] = False
                out.pop()

perm(0, M)