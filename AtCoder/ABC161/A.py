x,y,z = map(int,input().split())

w = x
x = y
y = w

w = x
x = z
z = w

print(x,y,z)