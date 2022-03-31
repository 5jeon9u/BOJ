def bingo_test():
    global ans
    # 사회자가 값을 부름
    for x in range(len(call)):
        # 빙고판 확인
        for y in range(5):
            for z in range(5):
                if call[x] == bingo[y][z]:
                    visit[y][z] = 1  # 빙고판에서 값 확인
                    check(y, z)  # 빙고 확인
                    if ans >= 3:  # 빙고가 3개가 된다면
                        return x + 1

def check(a, b):
    global ans

    r_cnt[a] += 1
    c_cnt[b] += 1

    if r_cnt[a] == 5:
        ans += 1
    if c_cnt[b] == 5:
        ans += 1

    if a == b:
        d_cnt[0] += 1
        if d_cnt[0] == 5:
           ans += 1

    if b == 4 - a:
        d_cnt[1] +=  1
        if d_cnt[1] == 5:
            ans += 1


bingo = [] # 빙고판
call = [] # 호출 순서
visit = [[0] * 5 for _ in range(5)] # 빙고판 체크
ans = 0 # 빙고를 외친 횟수

r_cnt = [0] * 5
c_cnt = [0] * 5
d_cnt = [0] * 2

for i in range(5):
    bingo.append(list(map(int, input().split())))

for j in range(5):
    dump = list(map(int, input().split()))
    for k in range(5):
        call.append(dump[k])

print(bingo_test())