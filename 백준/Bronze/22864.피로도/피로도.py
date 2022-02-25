A, B, C, M = map(int, input().split())
ret = 0
stress = 0
i = 1

if A > M:
    print(0)
else:
    while i < 25:
        i += 1
        if stress + A <=  M:
            ret += B
            stress += A
        else:
            if stress >= C:
                stress -= C
            else:
                stress = 0
    print(ret)