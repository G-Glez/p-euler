def problem45():
    hn = {n*(2*n-1) for n in range(100000)}
    pn = {n*(3*n-1)/2 for n in range(100000)}
    for i in hn & pn:
        if i > 40755:
            return i

if __name__ == "__main__":
    import time
    
    start_time = time.time()
    result = problem45()
    end_time = time.time()

    print(f"Result: {result}")
    print(f"Execution time: {end_time - start_time:.6f} seconds")