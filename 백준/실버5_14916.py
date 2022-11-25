N = int(input())
result = 0

if N <= 1:
    print(-1)

elif N % 5 == 0:
    result = N // 5
    print(result)

else:
    while N > 0:
        N -= 2
        result += 1
        if N % 5 == 0:
            result += N // 5
            N = 0
            print(result)
        elif N == 1:
            print(-1)
