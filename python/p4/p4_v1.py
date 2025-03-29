def problem4():
    upper_bound = 999
    lower_bound = 99

    palindrome = 0

    number = upper_bound
    while number > lower_bound and number * upper_bound > palindrome:
        prime = upper_bound
        while prime > lower_bound:
            if str(number * prime) == str(number * prime)[::-1] and number * prime > palindrome:
                palindrome = number * prime
            prime -= 1
        number -= 1
    return palindrome

if __name__ == "__main__":
    import time
    
    start_time = time.time()
    result = problem4()
    end_time = time.time()

    print(f"Result: {result}")
    print(f"Execution time: {end_time - start_time:.6f} seconds")