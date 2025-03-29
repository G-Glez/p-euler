def problem3():
    value = 600851475143

    largest_prime_number = 0

    number = 2
    while value != 1:
        if value % number == 0:
            value /= number
            largest_prime_number = number
        else:
            number += 1 if number == 2 else 2
    return largest_prime_number

if __name__ == "__main__":
    import time
    
    start_time = time.time()
    result = problem3()
    end_time = time.time()

    print(f"Result: {result}")
    print(f"Execution time: {end_time - start_time:.6f} seconds")