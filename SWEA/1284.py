T = int(input()) #테스트 케이스 값
A_result = 0
B_result = 0
result_arr = []

for i in range(1, T+1):
    T2 = list(map(int, input().split()))

    A_result = T2[0]*T2[4]
    if T2[4]<T2[2]:
        B_result = T2[1]
    else:
        B_result = (T2[4]-T2[2])*T2[3] + T2[1]
    
    if(A_result < B_result):
        result_arr.append(A_result)
    else:
        result_arr.append(B_result)

for i in range(1, T+1):
    print("#%d" %i,end =" ")
    print(result_arr[i-1])

# P  Q  R  S  W
# 9 100 20 3 10
# 한달에 10리터.
# A사의 경우 1L당 9원 => 10*9 = 90
# B사의 경우 20L 이하 => 100원 그 이후 1L당 10원 => 100 => 100 
# 8 300 100 10 250
# 한달에 250
# A사의 경우 1L당 8원 => 250*8 = 2000
# B사의 경우 100L 이하 => 300원 그 이후 1L당 10원 => 150*10+300 => 1800 
