quantidade = 0
positivos = 0
media = 0
for i in range(6):
    valor = float(input())
    if valor > 0:
      positivos += valor
      quantidade += 1
media = positivos / quantidade
print(f'{quantidade} valores positivos')
print(round(media,1))