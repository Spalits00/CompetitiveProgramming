N = int(input())
As = list(map(int, input().split()))
ct = [0] * N
     
for a in As: #ここがキモ．リスト「As」にはそれぞれの上司が入っていて，その中からaを取り出すので，a=上司になっている．これにより，ctの上司を正確に呼び出すことができる．
    ct[a-1] += 1
     
for c in ct:
    print(c)

#別解
#print(*c,sep='\n')