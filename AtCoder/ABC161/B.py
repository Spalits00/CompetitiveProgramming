n,m = map(int,input().split())
A = list(map(int,input().split()))
A.sort(reverse=True)
sortedA = list()
sum_of_votes = 0
for i in A : 
    sum_of_votes += i
for i in range(m) : #人気商品候補のsortedAリスト
    sortedA.append(A[i])
isOK = True
for i in sortedA: #人気商品候補のうち選べないものはないか？
    if i < sum_of_votes * (1/(4*m)) :
        isOK = False
if isOK == True :
    print("Yes")
else:
    print("No")