import sys
input = sys.stdin.readline

suNo,quizNo = map(int, input().split(" "))
numbers = list(map(int, input().split(" ")))

sum_arr = [0]
temp = 0

for i in numbers:
    temp = temp + i
    sum_arr.append(temp)

for i in range(quizNo):
    s, e = map(int, input().split())
    print(sum_arr[e] - sum_arr[s-1])