quant = 0
total = 0
while True:
    nota = float(input())
    if nota < 0.0 or nota > 10.0:
        print("nota invalida")
    else:
        total += nota
        quant += 1
    if quant == 2:
        media = total / quant
        break
print("media =",media)