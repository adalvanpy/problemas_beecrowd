x = int(input())
vezes = 0
while True:
    if x % 2 == 1:
        print(x)
        vezes +=1
    if vezes == 6:
        break
    x += 1

