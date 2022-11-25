import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
A = list(map(int, input().split()))
i = 0
j = N-1
count = 0

A.sort()

while i < j:
    if A[i] + A[j] < M: #합이 M 보다 작을경우 작은 숫자 인덱스 값 증가
        i += 1
    elif A[i] + A[j] > M: #합이 M 보다 클경우 큰 숫자 인덱스 값 감소
        j -= 1
    else: #그 외에는 카운트값 증가 및 작은 숫자 인덱스 값 증가, 큰 숫자 인덱스 값 감소
        count += 1
        i += 1
        j -= 1
print(count)