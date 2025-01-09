maior = 0
posicao = 0
for i in range(1,101):
    x = int(input())
    if maior < x:
        maior = x
        posicao = i
print(maior)
print(posicao)
