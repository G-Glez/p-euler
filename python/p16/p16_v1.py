def problem16():
    return sum([int(i) for i in str(pow(2, 1000))])

if __name__ == "__main__":
    import time
    
    start_time = time.time()
    result = problem16()
    end_time = time.time()

    print(f"Result: {result}")
    print(f"Execution time: {end_time - start_time:.6f} seconds")