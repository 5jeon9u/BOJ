def cut(check, direct, paper):
    lst = []
    # [1] 종이를 가로로 자르는 경우, 종이의 세로 길이가 변경 됨
    if check == 0:
        for j in range(len(paper)):
            if paper[j][2] < direct < paper[j][3]:
                x = paper[j]
                lst.append([x[0], x[1], x[2], direct])
                lst.append([x[0], x[1], direct, x[3]])
            else:
                lst.append(paper[j])
    # [2] 종이를 세로로 자르는 경우, 종이의 가로 길이가 변경 됨
    elif check == 1:
        for k in range(len(paper)):
            if paper[k][0] < direct < paper[k][1]:
                y = paper[k]
                lst.append([y[0], direct, y[2], y[3]])
                lst.append([direct, y[1], y[2], y[3]])
            else:
                lst.append(paper[k])

    return lst

N, M = map(int, input().split())
T = int(input())
# 처음 종이의 좌표
arr = [[0, N, 0, M]]
for i in range(T):
    A, B = map(int, input().split())
    arr = cut(A, B, arr)

# [3] 최대 넓이 찾기
max_cnt = 0
tot = 0
for l in range(len(arr)):
    tot = (arr[l][1] - arr[l][0]) * (arr[l][3] - arr[l][2])
    if max_cnt < tot:
        max_cnt = tot

print(max_cnt)