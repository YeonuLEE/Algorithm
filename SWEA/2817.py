T = int(input())

result = []

def solve(idx, sum):
    global cnt
    if idx >= N:
        return
    temp = sum + A[idx]
    if temp == K:
        cnt += 1

    solve(idx + 1, sum)
    solve(idx + 1, temp)

for i in range(T):
    N, K = map(int,input().split())
    A = list(map(int,input().split()))
    cnt = 0
    solve(0, 0)
    print("#{} {}".format(i+1, cnt))