class Calculator:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation

    def calculate(self):
        if self.operation == "add":
            return self.a + self.b

        elif self.operation == "sub":
            return self.a - self.b

        elif self.operation == "mul":
            return self.a * self.b

        elif self.operation == "div":
            if self.b != 0:
                return self.a / self.b
            else:
                return "Error: Division by zero"

        else:
            return "Invalid operation"


# Taking input from user
a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
operation = input("Enter operation (add/sub/mul/div): ")

# Create object of Calculator class
calc = Calculator(a, b, operation)

# Display result
result = calc.calculate()
print("Result:", result)
