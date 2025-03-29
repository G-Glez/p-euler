def problem7():
    def is_prime(number, prime_numbers):
        for i in prime_numbers:
            if number % i == 0:
                return False
        return True

    n = 10001
    prime_numbers = [2]
    current_number = 3
    while len(prime_numbers) != n:
        if is_prime(current_number, prime_numbers):
            prime_numbers.append(current_number)
        current_number += 2

    return prime_numbers[n - 1]

if __name__ == "__main__":
    import time
    
    start_time = time.time()
    result = problem7()
    end_time = time.time()

    print(f"Result: {result}")
    print(f"Execution time: {end_time - start_time:.6f} seconds")