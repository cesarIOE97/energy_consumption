import sys
sys.set_int_max_str_digits(0)

# fib_cache = {}  # Cache to store Fibonacci numbers

# def fibonacci(n):
#     if n <= 0:
#         return "Invalid input. Please provide a positive integer."
#     elif n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     elif n in fib_cache:
#         return fib_cache[n]
#     else:
#         fib_number = fibonacci(n - 1) + fibonacci(n - 2)
#         fib_cache[n] = fib_number
#         return fib_number

# if __name__ == '__main__':
#     num = int(sys.argv[1])
#     # for i in range(1,num):
#     #     result = fibonacci(i)
#     #     print("The Fibonacci number at position", i)
#     result = fibonacci(num)
#     print("The Fibonacci number at position", num, "is:", result)


def powLF(n):
    if n == 1:
        return (1, 1)
    L, F = powLF(n//2)
    L, F = (L**2 + 5*F**2) >> 1, L*F
    if n & 1:
        return ((L + 5*F) >> 1, (L + F) >> 1)
    else:
        return (L, F)


def fib(n):
    if n & 1:
        return powLF(n)[1]
    else:
        L, F = powLF(n // 2)
        return L * F

print (fib(int(sys.argv[1])))