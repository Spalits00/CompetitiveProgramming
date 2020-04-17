N,Y = map(int,input().split())
flag = False
for i in range(N+1):
    for j in range(N-i+1):
        if i * 10 + j * 5 + (N-i-j) * 1 == Y / 1000:
            flag = True
            print(i,j,N-i-j)
            if flag:
                break
    if flag:
        break
else:
    print("-1 -1 -1")