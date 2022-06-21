change = [list(map(int, input().split())) for _ in range(10)]

# 카드
card = []
for i in range(0, 21):
    card.append(i)

for tc in range(10): # 10번 반복
    start = change[tc][0]
    finish = change[tc][1]
    mid = (finish-start+1) // 2
    for k in range(mid):
        card[start + k], card[finish - k] = card[finish - k], card[start + k]

card.pop(0)
print(*card)
