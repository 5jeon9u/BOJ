x = int(input())
cnt = x # 전체 개수를 카운트

for i in range(x):
    word = input()
    lst = []  # 리스트에 단어를 차례대로 넣어서 연속을 확인
    for j in range(len(word)):
        if word[j] not in lst:
            lst.append(word[j])
        elif word[j] in lst:
            if word[j-1] == word[j]:
                pass
            else:
                cnt -= 1
                break
print(cnt)
