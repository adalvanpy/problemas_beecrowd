dia1 = int(input("Dia ")) 
hora1, minuto1, segundo1 = map(int, input().split(":")) 

dia2 = int(input("Dia ")) 
hora2, minuto2, segundo2 = map(int, input().split(":"))


inicio = dia1 * 86400 + hora1 * 3600 + minuto1 * 60 + segundo1
fim = dia2 * 86400 + hora2 * 3600 + minuto2 * 60 + segundo2


diferenca = (fim - inicio)


dias = diferenca // 86400

diferenca %= 86400

horas = diferenca // 3600

diferenca %= 3600

minutos = diferenca // 60

segundos = diferenca % 60


print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")