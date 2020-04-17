N = int(input())
a = list(map(int,input().split()))
alice = 0
bob = 0
for i in range(len(a) // 2):
    alice += a.pop(a.index(max(a)))
    bob += a.pop(a.index(max(a)))
if len(a) % 2 != 0:
    alice += a.pop(a.index(max(a)))
print(alice-bob)

