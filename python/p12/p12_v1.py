def problem12():
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

    class TriangleNumber:
        def __init__(self, seed, step):
            self.triangle_number = seed
            self.natural_number = step
            self.primes_below_50000 = primes_below(50000)

        def next(self):
            self.triangle_number += self.natural_number
            self.natural_number += 1

        def get_dividers(self):
            n_dividers = 1
            for i in self.factors().values():
                n_dividers *= (i + 1)
            return n_dividers + 1

        def factors(self):
            index = 0
            factors_of_n = {}
            n_aux = self.triangle_number
            while n_aux > 1:
                current_prime = self.primes_below_50000[index]
                if n_aux % current_prime == 0:
                    n_aux /= current_prime
                    if current_prime in factors_of_n.keys():
                        factors_of_n[self.primes_below_50000[index]] += 1
                    else:
                        factors_of_n[self.primes_below_50000[index]] = 1
                else:
                    index += 1
            return factors_of_n

    number = TriangleNumber(28, 8)
    while True:
        number.next()
        if number.get_dividers() >= 500:
            return number.triangle_number

if __name__ == "__main__":
    import time
    
    start_time = time.time()
    result = problem12()
    end_time = time.time()

    print(f"Result: {result}")
    print(f"Execution time: {end_time - start_time:.6f} seconds")