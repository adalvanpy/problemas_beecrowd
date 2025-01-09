cobaias = 0
coelhos = 0
ratos = 0
sapos = 0
n = int(input())
for i in range(n):
  x,y = input().split()
  x = int(x)
  cobaias += x
  if y == 'C':
    coelhos += x
  elif y == 'R':
    ratos += x
  elif y == 'S':
    sapos += x
print(f'Total: {cobaias} cobaias')
print(f'Total de coelhos: {coelhos}')
print(f'Total de ratos: {ratos}')
print(f'Total de sapos: {sapos}')
print(f'Percentual de coelhos: {(coelhos/cobaias) * 100:.2f} %')
print(f'Percentual de ratos: {(ratos/cobaias) * 100:.2f} %')
print(f'Percentual de sapos: {(sapos/cobaias) * 100:.2f} %')
