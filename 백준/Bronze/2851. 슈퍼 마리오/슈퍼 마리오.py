mushroom = [] # 버섯의 위치
mushroom_score = [] # 먹은 버섯과 점수의 차
total = 0 # 점수의 합
for i in range(10):
    mushroom.append(int(input()))

for j in range(10):
    total += mushroom[j]
    mushroom_score.append(100-total)

cnt = mushroom_score[0] # 최소 점수
for k in range(1, 10):
    if abs(cnt) >= abs(mushroom_score[k]):
        cnt = mushroom_score[k]

print(100-cnt)