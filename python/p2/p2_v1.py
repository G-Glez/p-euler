def problem2():
    max_value = 4000000

    res, fib1, fib2 = 0, 0, 1

    while fib2 < max_value:
        if fib2 % 2 == 0:
            res += fib2
        fib2, fib1 = fib2 + fib1, fib2
    return res

if __name__ == "__main__":
    print(problem2())