n,y = map(int,input().split())
     
n_max = int(y / 1000)
     
flag = True
     
if n <= n_max:
    for i in range(int((n_max - n)/9)+1):
        if (n_max - n - 9*i) % 4 == 0 and flag:
            b = int((n_max - n - 9*i)/4)
            c = n_max-10*i-5*b
            if c >= 0:
                print(i,b,c)
                flag = False
if flag:
    print('-1 -1 -1')