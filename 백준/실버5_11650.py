import sys
input = sys.stdin.readline

T = int(input())
arr = []

for i in range (T):
    arr.append(list(map(int,input().split())))

arr.sort(key = lambda x: (x[1],x[0]))

for k in arr:
    print(*k)