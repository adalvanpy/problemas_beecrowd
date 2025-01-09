n = int(input())
for i in range(n):
    x,y,z = map(float, input().split())
    media = ((x*2)+(y*3)+(z*5))/(2+3+5)
    print(round(media,1))
