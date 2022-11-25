testcase = int(input())
numbers = list(map(int, input().split(" ")))
max_number = max(numbers)
sum = sum(numbers)

print(sum * 100 / max_number / int(testcase))