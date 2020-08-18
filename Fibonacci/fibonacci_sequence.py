from functools import lru_cache


@lru_cache(maxsize=100)
def Fibonacci(n):
    if type(n) != int:
        raise TypeError("n precisa ser um inteiro")
    if n < 1:
        raise ValueError("n precisa ser um numero positivo")

    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

for n in range(1, 101):
    print(n, ":", Fibonacci(n))
