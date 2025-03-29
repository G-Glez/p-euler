def problem34():
    def factorial(n):
        fac = 1
        for i in range(1, n + 1):
            fac *= i
        return fac


    def factorialSum(vs):
        facSum = 0
        for i in vs:
            facSum += factorial(i)
        return facSum

    n = 1000000 #??????
    s = 0
    for i in range(3, n):
        if (i == factorialSum([int(n) for n in str(i)])):
            s += i
    return s

if __name__ == "__main__":
    import time
    
    start_time = time.time()
    result = problem34()
    end_time = time.time()

    print(f"Result: {result}")
    print(f"Execution time: {end_time - start_time:.6f} seconds")