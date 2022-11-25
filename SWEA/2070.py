T = int(input()) #테스트 케이스 값
result_arr = []

for i in range(1, T+1):
    T2 = list(map(int, input().split()))
    result = 0
    if T2[0]>T2[1]:
        result_arr.append(">")
    elif T2[0]<T2[1]:
        result_arr.append("<")
    else:
        result_arr.append("=")

for i in range(1, T+1):
    print("#%d" %i,end =" ")
    print(result_arr[i-1])