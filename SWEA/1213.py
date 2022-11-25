T = int(input())
count = 0

for i in range(T):
    str = input()
    str2 = input()
    count = str2.count(str)
    print("#{} {}".format(i+1, count))