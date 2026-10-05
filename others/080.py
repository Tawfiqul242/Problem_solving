# Handle invalid integer input

try:
    n = int(input("Enter an integer value: "))
    print(f"Value: {n}")

except ValueError:
    print("Invalid Input. Please! Enter an integer value.")