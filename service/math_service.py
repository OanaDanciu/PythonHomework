from functools import lru_cache


def power(a: int, b: int) -> int:
    return a ** b


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    return 1 if n == 0 else n * factorial(n - 1)


def sum_digits(n: int) -> int:
    if n < 0:
        n = abs(n)
    return sum(int(d) for d in str(n))


@lru_cache(maxsize=128)
def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers.")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
