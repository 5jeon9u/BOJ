N = int(input())
mountain = list(map(int, input().split()))
total = 0 #오르막길의 크기를 누적할 값
max_total = 0

for i in range(N-1):
    if mountain[i] < mountain[i + 1]:
        total += (mountain[i + 1] - mountain[i])
    else:
        total = 0
    if max_total < total:
        max_total = total

print(max_total)