N = int(input())
lst = []
total = 0 # 변경횟수의 누적 값
for i in range(N):
    lst.append(int(input()))

for j in range(N-1, 0, -1):
    if lst[j] <= lst[j-1]:
        total += (lst[j-1] - lst[j] + 1) # 감소시켜야 할 횟수
        lst[j-1] -= (lst[j-1] - lst[j] + 1) # 점수 감소

print(total)