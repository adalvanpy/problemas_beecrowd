doism = 2000.00
mil = 1000.00
milq = 1500.00
total = 0
valor = float(input())
if valor <= 2000.00:
  print('Isento')
if valor > 2000.00 and valor <= 3000.00:
  imposto = valor - doism
  imposto = imposto * 8 / 100
  total = imposto
  print(f"R$ {total:.2f}")
if valor > 3000.00 and valor <= 4500.00:
  imposto = valor - doism
  imposto = imposto - mil
  mil = mil * 8 /100
  imposto = imposto * 18 / 100
  total = mil + imposto
  print(f"R$ {total:.2f}")
  
if valor > 4500.00:
  imposto = valor - doism
  imposto = imposto - mil
  imposto = imposto - milq
  mil = mil * 8 /100
  milq = milq * 18 / 100
  imposto = imposto * 28 / 100
  total = mil + milq + imposto
  print(f"R$ {total:.2f}")

