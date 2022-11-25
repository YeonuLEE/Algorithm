from unittest import result


T = int(input())

result_arr = []

for i in range(0, T):
    result_arr.append(int(input()))

result_arr.sort()

for i in range(0, T):
    print(result_arr[i])