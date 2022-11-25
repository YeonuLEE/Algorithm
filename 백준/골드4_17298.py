import sys
input = sys.stdin.readline

N = int(input())
ans = [0] * N
A = list(map(int, input().split()))
Stack = []

for i in range(N):
    while Stack and A[Stack[-1]] < A[i]:
        ans[Stack.pop()] = A[i]
    Stack.append(i)

while Stack:
    ans[Stack.pop()] = -1

result = ""

for i in range(N):
    result += str(ans[i])+" "

print(result)