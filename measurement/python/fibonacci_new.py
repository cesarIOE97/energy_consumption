import sys
import decimal

def fibonacci(n):
    if n <= 0:
        return "Invalid input. Please provide a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        decimal.getcontext().prec = 100000  # Set precision for decimal calculations
        a, b = decimal.Decimal(0), decimal.Decimal(1)
        for _ in range(2, n):
            a, b = b, a + b
        return int(b)

if __name__ == '__main__':
    num = int(sys.argv[1])
    result = fibonacci(num)
    print("The Fibonacci number at position", num)
    print("The result is", result)
