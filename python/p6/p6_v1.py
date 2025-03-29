def problem6():
    first_n_numbers = 100

    sum_of_squares = sum([i ** 2 for i in range(first_n_numbers + 1)])
    square_of_sum = sum([i for i in range(first_n_numbers + 1)]) ** 2

    return square_of_sum - sum_of_squares

if __name__ == "__main__":
    import time
    
    start_time = time.time()
    result = problem6()
    end_time = time.time()

    print(f"Result: {result}")
    print(f"Execution time: {end_time - start_time:.6f} seconds")