def problem10():
    numbers = [i for i in range(0, 2000000)]

    i = 0
    while i < pow(len(numbers), .5):
        prime = numbers[i]
        if prime != 0 and prime != 1:
            for j in range(prime * 2, len(numbers), prime):
                numbers[j] = 0
        i += 1
    return sum(numbers) - 1

if __name__ == "__main__":
    import time
    
    start_time = time.time()
    result = problem10()
    end_time = time.time()

    print(f"Result: {result}")
    print(f"Execution time: {end_time - start_time:.6f} seconds")