N = int(input())
w_lst = [] # 몸무게 리스트
h_lst = [] # 키 리스트
total_lst = [1] * N # 등수 리스트

for i in range(0, N):
    x, y = map(int, input().split())
    w_lst.append(x)
    h_lst.append(y)

for j in range(0, N):
    for k in range(0, N):
        if w_lst[j] < w_lst[k]: # 현재 사람보다 몸무게가 큰 사람이
            if h_lst[j] < h_lst[k]: # 키도 크다면
                total_lst[j] += 1 # 등수가 하나 밀려남

for m in range(0, len(total_lst)):
    print(total_lst[m])