N = int(input())
A = []
B = []
yorokobi = []
for i in range(N):
    A.append(map(int,input().split()))
    B.append(A[i])
for i in range(N):
    if A.index(max(B)) == 0:
       continue
    else:
        yorokobi.append(A[i] * (A.index(max(B)) - A[i]))
        A[A.index(max(B))],A[i] = A[i],A[A.index(max(B))]
        B.remove(B.index(max(B)))
print(sum(yorokobi))
