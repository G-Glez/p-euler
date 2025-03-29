def problem35():
    def primes_below(n):
        numbers = [i for i in range(n)]
        i = 0
        while i < n:
            prime = numbers[i]
            if prime != 0 and prime != 1:
                for j in range(prime * 2, len(numbers), prime):
                    numbers[j] = 0
            i += 1
        return [i for i in numbers if i != 0 and i != 1]
    
    def rotation_numbers(n):
        rotations = []
        n_as_string = str(n)
        for i in range(len(n_as_string)):
            n_as_string = "".join(([n_as_string[i] 
                                    for i in range(1, len(n_as_string))]
                                   +[n_as_string[0]]))
            rotations.append(n_as_string)
        return list(map(int, rotations))
    
    def is_circular_prime(prime, primes):
        for rotation_number in rotation_numbers(prime):
            if rotation_number not in primes:
                return False
        return True
        
    def contains_even_numbers(number):
        for i in "02468":
            if i in str(number):
                return True
        return False
    
    primes_below_1000000 = primes_below(1000000)
    
    valid_primes_below_1000000 = [2]+[prime for prime in primes_below_1000000 if not contains_even_numbers(prime)] #append number 2, the even filter delete 2
    n_circular_primes = 0
    for prime in valid_primes_below_1000000:
        if is_circular_prime(prime, valid_primes_below_1000000):
            n_circular_primes += 1
    return n_circular_primes

if __name__ == "__main__":
    import time
    
    start_time = time.time()
    result = problem35()
    end_time = time.time()

    print(f"Result: {result}")
    print(f"Execution time: {end_time - start_time:.6f} seconds")