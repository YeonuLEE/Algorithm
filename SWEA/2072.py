T = int(input()) #테스트 케이스 값
result_arr = []

for i in range(1, T+1):
    T2 = list(map(int, input().split()))
    result = 0
    for j in range(0,10):
        if T2[j] % 2 != 0:
            result += T2[j]
        if j == 9:
            result_arr.append(result)

for i in range(1, T+1):
    print("#%d" %i,end =" ")
    print(result_arr[i-1])