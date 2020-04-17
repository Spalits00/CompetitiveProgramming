    #提出 #2297483 by itome
    
    # T の末尾に dream dreamer erase eraser のいずれかを追加する。
    s = input()
     
    ans = s.replace('eraser', '').replace('erase', '').replace('dreamer', '').replace('dream', '')
     
    if ans == '':
        print("YES")
    else:
        print("NO")