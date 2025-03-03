def fibonacci_any(n):
    if n < 0:
        return "Invalid input! Please enter a non-negative integer."
    elif n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Taking user input
n = int(input("Enter a number: "))
print(f"The {n}th Fibonacci number is: {fibonacci_any(n)}")
