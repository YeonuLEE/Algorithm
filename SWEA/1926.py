T = int(input()) #테스트 케이스 값
result_arr = []
cnt2 = 1

for i in range(1, T+1):
    cnt = 0
    result_arr.append(str(i))
    if ('3' not in result_arr[i-1])and('6' not in result_arr[i-1])and('9' not in result_arr[i-1]):
        print(result_arr[i-1], end=" ")

    if '3' in result_arr[i-1]:
        cnt += result_arr[i-1].count("3")
    if '6' in result_arr[i-1]:
        cnt += result_arr[i-1].count("6")
    if '9' in result_arr[i-1]:
        cnt += result_arr[i-1].count("9")
    for j in range(1,cnt+1):
        print("-",end="")
        if j==cnt:
            print(" ",end="")