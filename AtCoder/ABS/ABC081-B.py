N = int(input())
A = list(map(int,input().split()))
counter = 0
can = True
break_loop = False
while can:
    for i in A:
        if i % 2 == 0:
            can = True
        else:
            can = False
            print(counter)
            break_loop = True
            break
    if break_loop:
        break
    for i in A:
        A[A.index(i)] = i / 2
    counter += 1
else:
    print(counter)