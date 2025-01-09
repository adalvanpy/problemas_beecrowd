n = int(input())
mensagem = ''
for i in range(n):
    x = int(input())
    if x == 0:
        mensagem += 'NULL\n'
    elif x % 2 == 1 and x < 0:
        mensagem +='ODD NEGATIVE\n'
    elif x % 2 == 1 and x > 0:
        mensagem += 'ODD POSITIVE\n'
    elif x % 2 == 0 and x < 0:
         mensagem += 'EVEN NEGATIVE\n'
    elif x % 2 == 0 and x > 0:
         mensagem += 'EVEN POSITIVE'
print(mensagem)
