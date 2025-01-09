n = int(input())
for i in range(n):
    divisão = 0
    x,y = map(int,input().split())
    try:
        divisão = x/y
        print(divisão)
    except ZeroDivisionError:
        print("divisao impossivel")