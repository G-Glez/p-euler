def problem42():
    def num_value(string):
        value = 0
        for character in string:
            value += ord(character) - ord("A") + 1
        return value
    triangle_numbers = [n*(n+1)/2 for n in range(100)]
    file = open("data/0042_words.txt", "r")
    words = [word[1:-1] 
             for word in file.read().split(",")]
    values = [num_value(word) for word in words]
    return len([value for value in values if value in triangle_numbers])

if __name__ == "__main__":
    import time
    
    start_time = time.time()
    result = problem42()
    end_time = time.time()

    print(f"Result: {result}")
    print(f"Execution time: {end_time - start_time:.6f} seconds")