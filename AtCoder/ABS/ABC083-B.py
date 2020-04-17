N,A,B = map(int,input().split())
nums = []
ans = 0
for i in range(N):
    nums.append(N - i)
for i in nums:
    numSum = 0
    for j in str(i):
        numSum += int(j)
    if A <= numSum <= B:
        ans += i
print(ans)