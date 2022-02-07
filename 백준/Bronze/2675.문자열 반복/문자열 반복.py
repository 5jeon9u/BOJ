import sys
T = int(sys.stdin.readline())
for case in range(T):
    R, Test_case = sys.stdin.readline().split()
    word = ''
    for alpha in Test_case:
        word += alpha*int(R)
    print(word)