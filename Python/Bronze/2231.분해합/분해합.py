N = int(input())
min = N # 가장 작은 생성자를 저장할 변수

for i in range(1, N):
    K = i # 생성자 후보 변수
    M = i  # 생성자 후보 변수의 분해합을 저장할 변수
    while K > 0:
        M = M + (K % 10)
        K = (K // 10)
    if M == N and i < min:
        min = i

if min == N:
    print(0)
else:
    print(min)