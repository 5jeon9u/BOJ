N = int(input())

switch = [0] + list(map(int, input().split()))

S = int(input()) #총 학생수

for i in range(S):
    student, start = map(int, input().split())

    if student == 1:
         button = N // start
         for j in range(1, button+1):
             if switch[j * start] == 0:
                 switch[j * start] = 1
             else:
                 switch[j * start] = 0

    if student == 2:
        for k in range(0, start):
            if k + start <= N and start - k > 0 and switch[k + start] == switch[start - k]:
                if switch[k + start] == 0:
                    switch[k + start], switch[start - k] = 1, 1

                else:
                    switch[k + start], switch[start - k] = 0, 0
            else:
                break


result = [] #결과값 출력
for num in range(1, len(switch)):
    result.append(switch[num])
    if len(result) == 20:
        print(*result)
        result = []
if result:
    print(*result)