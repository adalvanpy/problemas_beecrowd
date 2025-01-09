n = int(input())
for i in range(n):
    soma = 0
    x,y = map(int, input().split())
    if x < y:
      while x < y:
         x += 1
         if x < y:
           if x % 2 == 1:
             soma += x
      print(soma)
    else:
       while x > y:
          x -= 1
          if x > y:
            if x % 2 == 1:
              soma += x
       print(soma)