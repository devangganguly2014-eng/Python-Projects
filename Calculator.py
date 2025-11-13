# Calculator program

# ⚙️ Advanced Calculator by Devang Ganguly

while True:
    print("\n----- Advanced Calculator -----")
    print("Available operators: +  -  *  /  %  **  //")
    print("Type 'exit' to quit\n")

    operator = input("Enter an operator: ")

    if operator.lower() == "exit":
        print("👋 Thanks for using Devang's Calculator!")
        break

    if operator not in ["+", "-", "*", "/", "%", "**", "//"]:
        print("❌ Invalid operator! Try again.")
        continue

    # Input numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform operation
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("⚠️ Error: Division by zero is not allowed.")
            continue
    elif operator == "%":
        result = num1 % num2
    elif operator == "**":
        result = num1 ** num2
    elif operator == "//":
        if num2 != 0:
            result = num1 // num2
        else:
            print(" Error: Division by zero is not allowed.")
            continue

    print(f"Result: {round(result, 4)}")
