import sys
input = sys.stdin.readline

S = int(input())
N = 0
sum = 0

while S >= sum:
    N += 1
    sum += N
    if sum > S:
        break
print(N-1)