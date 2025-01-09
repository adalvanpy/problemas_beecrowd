a = 0
b = 1
n = int(input())
print(f"{a} {b}", end=" ")
for i in range(0,n):
    temp = a + b
    if i == n:
      print(temp,end="")
    else:
      print(temp,end=" ")
    a = b
    b = temp
print()
