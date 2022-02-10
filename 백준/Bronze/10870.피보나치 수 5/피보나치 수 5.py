def fibo(x):
    if x < 2:
        return x
    else:
        return fibo(x-2) + fibo(x-1)

y = int(input())

print(fibo(y))