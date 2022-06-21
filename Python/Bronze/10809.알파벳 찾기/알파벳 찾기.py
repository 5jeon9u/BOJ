S = input()

for i in range(97, 123):
    for j in range(0, len(S)):
        num = -1
        if i == ord(S[j]):
            num = j
            break
    print(num, end=' ')