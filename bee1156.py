a = 1
b = 1
s = 0
n = 1
for i in range(3,40):
    if i % 2 == 1:
      c = a + b
      s += n + i / c
      a = c
      b = c
      n = 0
    
print(f"{s:.2f}")