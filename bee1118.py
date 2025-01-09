total = 0
quant = 0
parar = 0
while True:
    if parar == 2:
        break
    nota = float(input())
    if nota < 0.0 or nota > 10.0:
        print("nota invalida")
    else:
        total += nota
        quant += 1
    if quant == 2:
        media = total / quant
        print(f"media = {media:.2f}")
        print("novo calculo (1-sim 2-nao)")
        while True:
          novo = int(input())
          if novo < 1 or novo > 2:
            print("novo calculo (1-sim 2-nao)")   
          elif novo == 1:
            total = 0
            quant = 0
            break
          elif novo == 2:
            parar += 2
            break

