A, B = input().split()
a, b = 0, 0
matrix = [['.'] * len(A) for _ in range(len(B))]

for i in range(len(A)): # 중복 글자 찾기
    if A[i] in B:
        a = i
        break

for j in range(len(B)):
    if A[a] == B[j]:
        b = j
        break

for m in range(len(A)):
    matrix[b][m] = A[m]

for n in range(len(B)):
    matrix[n][a] = B[n]

for i in range(len(B)):
    for j in range(len(A)):
        print(matrix[i][j], end='')
    print()