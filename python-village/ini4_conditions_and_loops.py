num1 = int(input())
num2 = int(input())

sum_odd_nums = 0
for i in range(num1, num2 + 1):
    if i % 2 != 0:
        sum_odd_nums += i

print(sum_odd_nums)