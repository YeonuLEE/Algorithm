T = int(input())

for i in range(1, T+1):
    A = input()
    N = "0"
    count = 0

    for j in range(len(A)):
        if A[j] != N:
            N = A[j]
            count += 1

    print("#{} {}".format(i+1, count))