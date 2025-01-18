numero_teste = int(input())

for i in range(numero_teste):
  populacao_a,populacao_b, taxa_a, taxa_b = input().split() 
  populacao_a = int(populacao_a)
  populacao_b = int(populacao_b)
  taxa_a = float(taxa_a)
  taxa_b = float(taxa_b)
  anos = 0

  while populacao_a <= populacao_b:
    crescimento_b = int(populacao_b * taxa_b / 100) 
    crescimento_a = int(populacao_a * taxa_a / 100) 
    populacao_a = populacao_a + crescimento_a
    populacao_b = populacao_b + crescimento_b
    anos += 1
    if anos > 100:
      print("Mais de 1 seculo.")
      break
  if anos <= 100:
      print(f"{anos} anos.")


