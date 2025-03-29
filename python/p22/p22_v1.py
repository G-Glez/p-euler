def problem22():
    def num_value(string):
        value = 0
        for character in string:
            value += ord(character) - ord("A") + 1
        return value
    file = open("data/0022_names.txt", "r")
    names = [name[1:-1] 
             for name in file.read().split(",")]
    names.sort()
    values = [num_value(names[index])*(index +1) 
              for index in range(len(names))]
    return sum(values)

if __name__ == "__main__":
    import time
    
    start_time = time.time()
    result = problem22()
    end_time = time.time()

    print(f"Result: {result}")
    print(f"Execution time: {end_time - start_time:.6f} seconds")