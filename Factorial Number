def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        fact = factorial(num)
        print(f"The factorial of {num} is {fact}")
    except ValueError as e:
        print(e)
