def switch(x):
    if light[x] == 0:
        light[x] = 1
    else:
        light[x] = 0

N = int(input()) # 전구의 수
light = [0] + list(map(int, input().split())) # 전구 상태
cnt = int(input()) # 학생 수

# [1] 학생들의 스위치 조작
for i in range(cnt):
    sex, num = map(int, input().split())

    # [2] 남학생일 경우
    if sex == 1:
        n = 1
        # 상태를 바꿀 전구는 전구의 수 범위 내에 있어야 함
        while num * n <= N:
            switch(num * n)
            n += 1
    # [3] 여학생일 경우
    elif sex == 2:
        switch(num)
        l = 1
        # 상태를 바꿀 전구는 전구의 수 범위 내에 있어야 함
        # 받은 스위치 번호를 기준으로 좌우가 대칭이어야 함
        while 0 < num - l and num + l <= N and light[num - l] == light[num + l]:
            switch(num - l)
            switch(num + l)
            l += 1

for i in range(1, N+1):
    print(light[i], end = ' ')
    if i % 20 == 0 :
        print()