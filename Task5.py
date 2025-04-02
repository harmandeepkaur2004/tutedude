def factorial(n):
    """Calculates the factorial of a given number using recursion."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("\033[95mEnter a number:\033[0m "))

fact = factorial(num)

print(f"\n\033[95mFactorial of {num} is: {fact}\033[0m")
