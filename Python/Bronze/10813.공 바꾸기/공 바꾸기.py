#바구니의 수 N, 교환 횟수 M
N, M = map(int, input().split())

# 바구니 생성
basket = [0] * (N+1)

# 바구니에 공 채우기
for k in range(1, N+1):
    basket[k] = k

for tc in range(1, M+1):
    i, j = map(int, input().split())

    basket[i], basket[j] = basket[j], basket[i]

print(*basket[1:])