z = 0
a,n = map(int,input().split())
while n <= 0:
  n = int(input())
for i in range(n-1,-1,-1):
  z += (a+i)
print(z)
