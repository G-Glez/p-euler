def problem21():
    def primes_below(n):
        numbers = [i for i in range(n)]
        i = 0
        while i < pow(len(numbers), .5):
            prime = numbers[i]
            if prime != 0 and prime != 1:
                for j in range(prime * 2, len(numbers), prime):
                    numbers[j] = 0
            i += 1
        return [i for i in numbers if i != 0 and i != 1]

    def factors(n):
        primes_below_5000 = primes_below(5000)
        index = 0
        factors_of_n = {}
        n_aux = n
        while primes_below_5000[index] <= n // 2:
            current_prime = primes_below_5000[index]
            if n_aux % current_prime == 0:
                n_aux /= current_prime
                if current_prime in factors_of_n.keys():
                    factors_of_n[primes_below_5000[index]] += 1
                else:
                    factors_of_n[primes_below_5000[index]] = 1
            else:
                index += 1
        return factors_of_n

    return factors(254)
    amicable_numbers = []
    non_amicable_numbers = []

if __name__ == "__main__":
    import time
    
    start_time = time.time()
    result = problem21()
    end_time = time.time()

    print(f"Result: {result}")
    print(f"Execution time: {end_time - start_time:.6f} seconds")