soma = 0
cont = 0
inicio = 0
n = int(input())
for i in range(n):
    x,y = map(int,input().split())
    while True:
        if x % 2 == 1:
          soma += x
          cont += 1
        x += 1
        if cont == y:
            break
    print(soma)
    soma = 0
    cont = 0
