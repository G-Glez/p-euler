def problem2():
    max_value = 4000000

    res, fib1, fib2 = 0, 0, 1

    while fib2 < max_value:
        if fib2 % 2 == 0:
            res += fib2
        fib2, fib1 = fib2 + fib1, fib2
    return res

if __name__ == "__main__":
    import time
    
    start_time = time.time()
    result = problem2()
    end_time = time.time()

    print(f"Result: {result}")
    print(f"Execution time: {end_time - start_time:.6f} seconds")