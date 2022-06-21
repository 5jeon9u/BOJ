N, M = map(int, input().split())
lst = []  # 출력 내용
visited = [False] * (N+1)

def perm(start):
    if len(lst) == M: # 2개의 수만을 취함
        print(*lst)
        return
    else:
        for i in range(start, N+1):
            lst.append(i)
            perm(i)
            lst.pop()

perm(1)