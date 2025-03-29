def problem40():
    decimals = ""
    i, product1n = 1, 1
    while len(decimals) < 1000000:
        decimals += str(i)
        i += 1
    for i in [10 ** n for n in range(7)]:
        product1n *= int(decimals[i - 1])
    return product1n

if __name__ == "__main__":
    import time
    
    start_time = time.time()
    result = problem40()
    end_time = time.time()

    print(f"Result: {result}")
    print(f"Execution time: {end_time - start_time:.6f} seconds")