A,B,C = map(int,input().split())
ans = 1
coins = 0
for i in range(1000000):
    if ans % 7 == 0:
        coins += B
    coins += A
    if coins >= C:
        print(ans)
        break
    ans += 1