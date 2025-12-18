# Take input from user
a = int(input("Enter a number: "))

# If a is even, reduce it by 1
if a % 2 == 0:
    a = a - 1

# Generate and print odd numbers
for i in range(1, a + 1):
    print(2 * i - 1, end=" ")
