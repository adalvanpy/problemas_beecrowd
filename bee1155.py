n = 1
s = 0
for i in range(2,101):
    s += n + 1 / i
    n = 0
print(f"{s:.2f}")
