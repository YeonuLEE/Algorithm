T = int(input())

result_arr = []

for i in range(0, T):
    str = input()
    result_arr.append((len(str), str))
result_arr = list(set(result_arr))
result_arr.sort()

for str_len, str in result_arr:
    print(str)