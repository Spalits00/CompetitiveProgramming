import re
S = input()
while S != "":
    if re.match('dream',S):
        if not re.match('dreamera',S):
            if re.match('dreamer',S):
                S = S.replace('dreamer','',1) #「=」を忘れない．lstrip関数は値を返すだけ
            else:
                S = S.replace('dream','',1)
        else:
            S = S.replace('dream','',1)
    elif re.match('erase',S):
        if re.match('eraser',S):
            S = S.replace('eraser','',1)
        else:
            S = S.replace('erase','',1)   
    # elif re.match('dreamer',S) and re.match("^(?!dreamera)",S):
    #     S = S.replace('dreamer','',1)      
    else:
        print("NO")
        exit(0)
else:
    print("YES")
    

