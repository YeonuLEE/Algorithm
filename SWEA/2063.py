import sys
sys.stdin = open("input.txt","r")
T = int(input()) #테스트 케이스 값
result_arr = []

for i in range(1, T+1):
    T2 = list(map(int, input().split()))
    Max_number = 0
    for j in range (0, 9):
        if T2[j] > Max_number:
            Max_number = T2[j]
    result_arr.append(Max_number)

for i in range(1, T+1):
    print("#%d" %i,end =" ")
    print(result_arr[i-1])