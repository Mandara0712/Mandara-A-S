# Given input list
numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]

# Dictionary to store result
result = {}

# Check multiples from 1 to 9
for i in range(1, 10):
    count = 0
    for num in numbers:
        if num % i == 0:
            count += 1
    result[i] = count

# Print the output dictionary
print(result)
