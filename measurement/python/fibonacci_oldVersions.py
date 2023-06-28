import sys

def fibonacci(n):
    if n <= 0:
        return "Invalid input. Please provide a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib_sequence = [0, 1]  # List to store Fibonacci sequence
        for i in range(2, n):
            next_number = fib_sequence[i - 1] + fib_sequence[i - 2]
            fib_sequence.append(next_number)
        return fib_sequence[n - 1]

if __name__ == '__main__':
    num = int(sys.argv[1])
    # for i in range(506990,num):
    #     result = fibonacci(i)
    #     print("The Fibonacci number at position", i)
    result = fibonacci(num)
    print("The Fibonacci number at position", num)