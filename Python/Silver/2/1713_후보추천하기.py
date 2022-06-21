import sys
sys.stdin = open('input.txt')

N = int(input()) # 사진틀의 개수
num = int(input()) # 전체 학생의 총 추천 횟수
student = list(map(int, input().split())) # 추천받은 학생을 나타내는 번호

# 후보자이름 : [추천 수, 들어온 순서]
photo = {}

for i in range(num):

    # 사진틀에 해당 학생이 있을 경우
    if student[i] in photo:
        photo[student[i]][0] += 1

    # 사진틀에 해당 학생이 없을 경우
    else:
        # 사진틀에 자리가 있는지 확인
        if len(photo) < N: # 자리가 있는 경우
            photo[student[i]] = [1, i]
        else: # 자리가 없는 경우
            # 삭제할 학생을 고르기 위해 정렬(추천수가 적고, 오래된 사진)
            del_list = sorted(photo.items(), key = lambda x : (x[1][0], x[1][1]))
            del_key = del_list[0][0]
            del(photo[del_key])
            photo[student[i]] = [1, i]

ans_list = sorted(photo.keys())
print(*ans_list)
