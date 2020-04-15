A = int(input())
B = int(input())
C = int(input())
X = int(input())
counter = 0
if 500 <= X:
    for i in range(A):
        if 500*(i+1) < X:
            for j in range(B):
                if 100*(j+1) < X - 500*(i+1):
                    for k in range(C):
                        if 50*(k+1) == X - 500*(i+1) - 100*(j+1):
                            counter += 1
                if 100*(j+1) == X - 500*(i+1):
                    counter += 1
            for k in range(C):
                if 50*(k+1) == X - 500*(i+1):
                    counter += 1
        if 500*(i+1) == X:
            counter += 1
if 100 <= X:
    for i in range(B):
        if 100*(i+1) < X:
            for j in range(C):
                if 50*(j+1) == X - 100*(i+1):
                    counter += 1
        if 100*(i+1) == X:
            counter += 1
if 50 <= X:
    for i in range(C):
        if 50*(i+1) == X:
            counter += 1
print(counter)