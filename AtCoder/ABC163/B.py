N,M = map(int,input().split())
A = map(int,input().split())
shukudai_kakarujikann = sum(A)
if shukudai_kakarujikann > N:
    print("-1")
    exit(0)
else:
    print(N - shukudai_kakarujikann)