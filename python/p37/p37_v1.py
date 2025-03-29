def problem37():
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
    
    def is_truncatable_candidate(number):
        for i in "468":
            if i in str(number):
                return False
        if (number == 2 
                or number == 3 
                or number == 5 
                or number == 7):
            return False
        return True
    
    def truncatable_list(number):
        truncatable = []
        for i in range(len(str(number))):
            truncatable.append(str(number)[0:i+1])
            truncatable.append(str(number)[i:len(str(number))])
        return list(map(int, set(truncatable)))
    
    def is_truncatable_number(number, primes):
        for item in truncatable_list(number):
            if item not in primes:
                return False
        return True
        
    primes_below_10000 = primes_below(1000000)
    valid_primes_below_10000 = [prime for prime in primes_below_10000 if is_truncatable_candidate(prime)]
    truncatable_numbers = [prime for prime in valid_primes_below_10000 if is_truncatable_number(prime, primes_below_10000)]
    
    return sum(truncatable_numbers)

if __name__ == "__main__":
    import time
    
    start_time = time.time()
    result = problem37()
    end_time = time.time()

    print(f"Result: {result}")
    print(f"Execution time: {end_time - start_time:.6f} seconds")