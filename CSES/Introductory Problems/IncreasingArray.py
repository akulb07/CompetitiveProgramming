n = int(input(""))
count = 0
numbers = list(map(int, input("").split()))

for i in range(1, len(numbers)):
    if numbers[i] < numbers[i - 1]:
        count += numbers[i - 1] - numbers[i]
        numbers[i] = numbers[i - 1]

print(count)