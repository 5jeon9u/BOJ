A, B, C, M = map(int, input().split())
cnt = 0
tired = 0
done = 0

if A > M :
    print(0)
else:
    while cnt < 24:
        cnt += 1
        if tired <= M - A:
            done += B
            tired += A
        else:
            if tired - C >= 0:
                tired -= C
            else:
                tired = 0
    print(done)