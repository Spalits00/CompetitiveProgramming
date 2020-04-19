import sys
sys.setrecursionlimit(4100000)
input = sys.stdin.readline
N = int(input()) #社員数
joushi_no_bangou = [0] #上司の社員番号
ans = []
joushi_no_bangou += map(int,input().split())
for i in range(N):
    print(joushi_no_bangou.count(i+1))