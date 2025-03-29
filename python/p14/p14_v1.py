def problem14():
    def next(n):
        if n % 2:
            return 3 * n + 1
        else:
            return n / 2

    class ChainCache:
        def __init__(self):
            self.cache = {}

        def __call__(self, n):
            if n == 1:
                return 1
            elif n in self.cache:
                return self.cache[n]
            else:
                c = self.__call__(next(n))
                self.cache[n] = c + 1
                return c + 1

    chain_len = ChainCache()

    def maxlen(x):
        m = 0
        v = 0
        for i in range(1, x):
            l = chain_len(i)
            if l > m:
                m = l
                v = i
        return v, m

    maxlen(1000000)

if __name__ == "__main__":
    import time
    
    start_time = time.time()
    result = problem14()
    end_time = time.time()

    print(f"Result: {result}")
    print(f"Execution time: {end_time - start_time:.6f} seconds")