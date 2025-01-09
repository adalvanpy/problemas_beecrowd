x,y = map(int,input().split())
z = x
for i in range(1,y+1):
    if i == x:
      print(f"{i}", end="")
    else:
      print(f"{i} ", end="")
    if x == i:
        print()
        x+=z