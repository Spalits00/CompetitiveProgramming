myList = list(map(int,input().split()))
myList.sort()
# for i in myList:
#     print(i,end = ' ')
print(*myList, sep = ' ')