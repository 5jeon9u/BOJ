#flag를 꽂을 리스트 10000개
num_list = [True for i in range(1, 10001)]

# 각 자릿수 이므로 몇 자릿 수인지 판별
def d(n):
    while True:
        num = 0
        #1의 자릿수일 떄,
        if n // 10 == 0:
            num = n + n
            num_list[num] = False
            break
        # n이 10의 자릿수 일 때,
        elif n // 100 ==0:
            num = n + (n //10)%10 + n%10
            num_list[num] = False
            break
        # n이 100의 자릿수 일 때,
        elif n // 1000 ==0:
            num = n + (n//100)%10 +(n //10) %10 + n%10
            num_list[num] = False
            break
        # n이 1000의 자릿수 일 때, 9999를 넣으면 10000을 넘는 것 예외처리
        elif n // 10000 ==0:
            num = n + (n//1000)%10 + (n//100)%10 +(n //10) %10 + n%10
            if num >= 10000:
                break
            else:    
                num_list[num] = False
                break
        elif n ==10000:
            num_list[num] = False
            break
for i in range(1, 10001):
        d(i)

result_list = list(filter(lambda x: num_list[x] == True, range(len(num_list))))

for i in result_list:
    print(i)