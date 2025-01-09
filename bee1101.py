while True:
    soma = 0
    try:
      m,n = map(int, input().split())
    except EOFError:
      print('EOF when reading a line')
      
    if m <= 0 or n <= 0:
      break
    if m < n:
      for i in range(m,n + 1):
        print(i, end=" ")
        soma += i
    else:
      for i in range(n,m + 1):
        print(i, end=" ")
        soma += i     
    print(f' SUM={soma}')
