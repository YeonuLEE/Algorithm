import sys
sys.stdin = open("input.txt","r")
T = int(input())

for testcase in range(T):
    N, M = map(int, input().split())
    if N > M:
        Big = N
        Small = M
        Aj = list(map(int, input().split()))
        Bj = list(map(int, input().split()))
    else:
        Big = M
        Small = N
        Bj = list(map(int, input().split()))
        Aj = list(map(int, input().split()))
    result=-float('inf')
    for i in range(Big-Small+1):
        Max = 0
        for j in range(Small):
            Max += Bj[j] * Aj[j+i]
        if Max > result:
            result = Max

    print("#{} {}".format(testcase+1, result))