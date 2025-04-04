def problem1():
    return sum([i
                for i in range(1000)
                if (i % 3 == 0 or i % 5 == 0)])

if __name__ == "__main__":
    import time
    
    start_time = time.time()
    result = problem1()
    end_time = time.time()

    print(f"Result: {result}")
    print(f"Execution time: {end_time - start_time:.6f} seconds")