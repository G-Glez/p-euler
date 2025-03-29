def problem25():
    fib1, fib2, index = 1, 1, 2
    while len(str(fib2)) != 1000:
        index += 1
        fib2, fib1 = fib2 + fib1, fib2
        if len(str(fib2)) == 1000:
            return index

if __name__ == "__main__":
    import time
    
    start_time = time.time()
    result = problem25()
    end_time = time.time()

    print(f"Result: {result}")
    print(f"Execution time: {end_time - start_time:.6f} seconds")