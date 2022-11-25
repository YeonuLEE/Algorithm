T = int(input())
Arr = [0]*T

for i in range(T):
    Arr[i] = int(input())

for i in range(T-1):
    for j in range(T-1-i):
        if Arr[j] > Arr[j+1]:
            temp = Arr[j]
            Arr[j] = Arr[j+1]
            Arr[j+1] = temp

for i in range(T):
    print(Arr[i])