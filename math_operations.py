import sys

# Ensure the correct number of arguments is received
if len(sys.argv) != 4:
    print("<h3>Error: Invalid number of arguments.</h3>")
    sys.exit(1)

try:
    # Retrieve user inputs
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
    operation = sys.argv[3]
except ValueError:
    print("<h3>Error: Invalid input format. Please enter numerical values.</h3>")
    sys.exit(1)

# Perform the selected operation
if operation == "add":
    result = num1 + num2
elif operation == "sub":
    result = num1 - num2
elif operation == "mul":
    result = num1 * num2
elif operation == "div":
    if num2 == 0:
        print("<h3>Error: Division by zero is not allowed.</h3>")
        sys.exit(1)
    result = num1 / num2
else:
    print("<h3>Error: Invalid operation selected.</h3>")
    sys.exit(1)

# Apply additional conditions
if result > 100:
    result *= 2
elif result < 0:
    result += 50

# Generate HTML output
print(f"""
<h3>Math Operation Result:</h3>
<p>Calculation result: {result:.2f}</p>
""")
