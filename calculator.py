# Create a calculator

# Define
def calculator(num_1, num_2, op):
    result = 0

    if op == "+":
        result = num_1 + num_2

    elif op == "-":
        result = num_1 - num_2

    elif op == "*":
        result = num_1 * num_2

    elif op == "/":
        result = num_1 / num_2

    print(f"{num_1} {op} {num_2} = {result}")

# Test
calculator(5, 10, "*")
calculator(2021, 1984, "-")
calculator(25, 5, "/")
calculator(12, 34, "+")
