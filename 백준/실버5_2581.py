def is_true_number(N,N2):
    if N < 10000 and N2 < 10000 and N <= N2:
        return True
    else:
        return False

Min = int(input())
Max = int(input())

is_true_number(Min,Max)

Sum_result = 0
Min_result = 0
cnt = 0

def is_prime_num(n):
    if(n == 1):
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for i in range(Min,Max+1):
    if(is_prime_num(i)):
        Sum_result += i
        cnt += 1
        if(cnt == 1):
            Min_result = i
        
if(cnt > 0):
    print(Sum_result)
    print(Min_result)    

elif(cnt == 0):
    print(-1)