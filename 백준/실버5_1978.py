T = int(input())

def is_prime_num(n):
    if(n == 1):
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def is_true_number(N,N2):
    if N == len(N2) and N < 100:
        return True
    else:
        return False

cnt = 0
T2 = input().split()

is_true_number(T,T2)

for i in range(0, T):
    if is_prime_num(int(T2[i])) :
        cnt += 1

print(cnt)