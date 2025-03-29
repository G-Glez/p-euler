def problem20():
    factorial = 1
    for i in range(1, 101):
        factorial *= i
    return sum([int(i) for i in str(factorial)])

if __name__ == "__main__":
    import time
    
    start_time = time.time()
    result = problem20()
    end_time = time.time()

    print(f"Result: {result}")
    print(f"Execution time: {end_time - start_time:.6f} seconds")