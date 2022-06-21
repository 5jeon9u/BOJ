# N장의 카드 중 3장을 선택하여 M을 넘지 않으면서 가장 가깝게 만드는 카드의 합을 구하시오

N, M = map(int, input().split())
card = list(map(int, input().split()))

# 카드 3장의 합을 구해 저장할 리스트
card_sum = []
test_lst = []
sum = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if card[i] + card[j] + card[k] > M:
                continue
            else:
                card_sum.append(card[i] + card[j] + card[k])
max = 0
for n in range(len(card_sum)):
    if max < card_sum[n]:
        max = card_sum[n]

print(max)

