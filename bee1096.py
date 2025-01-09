x = 1
y = 7
while True:
    for i in range(3):
        print(f'I={x} J={y-i}')
    if x == 9:
      break
    x += 2
    