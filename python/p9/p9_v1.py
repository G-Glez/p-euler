def problem9():
    n = 1000
    res = 0

    a_range = n - 3
    for a in range(3, a_range):
        b_range = a_range - a
        for b in range(2, b_range + 1):
            c = n - a - b
            if a ** 2 + b ** 2 == c ** 2:
                res = a * b * c
    return res

if __name__ == "__main__":
    import time
    
    start_time = time.time()
    result = problem9()
    end_time = time.time()

    print(f"Result: {result}")
    print(f"Execution time: {end_time - start_time:.6f} seconds")