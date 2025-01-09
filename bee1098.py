x = 0
y = 1
while True:
    for i in range(3):
        if x % 1 == 0.0 or y % 1 == 0.0:
          print(f'I={round(x)} J={round(y+i)}')
        else:
          print(f'I={x} J={y+i}')
    if x == 2.0:
        break
    x = round(x + 0.2, 1)
    y = round(y + 0.2, 1)
   