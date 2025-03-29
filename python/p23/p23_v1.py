def problem23():
    def is_abundant(number):
        return sum(i for i in range(1, number//2+1) if number%i == 0) > number
    
    def is_sum_of_two_abundant(number, abundant):
        return any(number-a in abundant for a in abundant)
    
    abundant_below_28123 = set(i for i in range(28123) if is_abundant(i))
    return sum([i for i in range(28123) if not is_sum_of_two_abundant(i, abundant_below_28123)])

if __name__ == "__main__":
    import time
    
    start_time = time.time()
    result = problem23()
    end_time = time.time()

    print(f"Result: {result}")
    print(f"Execution time: {end_time - start_time:.6f} seconds")