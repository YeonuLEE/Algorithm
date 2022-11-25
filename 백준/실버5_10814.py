T = int(input())

result_arr = []

for i in range(0, T):
    T2 = input().split()
    result_arr.append([int(T2[0]),T2[1]])

result_arr.sort(key=lambda x:x[0])

for i in range(0, T):
    print(result_arr[i][0],end=" ")
    print(result_arr[i][1])