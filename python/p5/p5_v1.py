def problem5():
    from functools import reduce

    to = 20

    factors = [0 for _ in range(to)]

    for number in range(1, to + 1):
        counter = 2
        current_factors = [0 for _ in range(number)]
        while number != 1:
            if number % counter == 0:
                number /= counter
                current_factors[counter - 1] += 1
            else:
                counter = counter + 1 if counter == 2 else counter + 2
        for number in range(len(current_factors)):
            if current_factors[number] > factors[number]:
                factors[number] = current_factors[number]

    return reduce(lambda x, y: x * y, [i ** factors[i - 1] for i in range(1, 20 + 1)])

if __name__ == "__main__":
    import time
    
    start_time = time.time()
    result = problem5()
    end_time = time.time()

    print(f"Result: {result}")
    print(f"Execution time: {end_time - start_time:.6f} seconds")