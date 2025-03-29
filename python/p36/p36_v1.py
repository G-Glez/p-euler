def problem36():
    sum = 0
    for i in range(1000000):
        if str(i) == str(i)[::-1] and bin(i)[2:] == bin(i)[2:][::-1]:  #I know this is unreadable xD
            sum += i
    return sum

if __name__ == "__main__":
    import time
    
    start_time = time.time()
    result = problem36()
    end_time = time.time()

    print(f"Result: {result}")
    print(f"Execution time: {end_time - start_time:.6f} seconds")