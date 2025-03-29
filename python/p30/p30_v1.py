def problem30():
    """
    We can find out the maxim possible sum for a given number of digits by multiplying
    9^5 by the number of digits. If 9^5 * number of digits < number, wont find any other
    number which full fill the condition
    """
    v = []
    i = 2
    while (True):
        i += 1
        if (i == sum([pow(int(j), 5) for j in str(i)])):
            v.append(i)
        if (pow(9, 5) * len(str(i)) < i):
            break
    return sum(v)

if __name__ == "__main__":
    import time
    
    start_time = time.time()
    result = problem30()
    end_time = time.time()

    print(f"Result: {result}")
    print(f"Execution time: {end_time - start_time:.6f} seconds")