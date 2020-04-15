S = input()
charsList = list()
for char in S :
    charsList.append(char)
if charsList[2] == charsList[3] :
    if charsList[4] == charsList[5] :
        print("Yes")
    else :
        print("No")
else :
    print("No")