def problem29():
    return len({a**b 
                for a in range(2,101) 
                for b in range(2,101)})

if __name__ == "__main__":
    import time
    
    start_time = time.time()
    result = problem29()
    end_time = time.time()

    print(f"Result: {result}")
    print(f"Execution time: {end_time - start_time:.6f} seconds")