n = int(input())
k = int(input())

rabbits = [1, 1]
for i in range(1, n - 1):
    rabbits.append(rabbits[i] + (rabbits[i - 1] * k))

print(rabbits[-1])