package main

import (
	"fmt"
	"time"
)

func problem2() int {
	const maxValue int = 4000000

	result, fib1, fib2 := 0, 1, 2

	for fib2 < maxValue {
		if fib2%2 == 0 {
			result += fib2
		}
		fib1, fib2 = fib2, fib1+fib2
	}

	return result
}

func main() {
	start := time.Now()
	fmt.Println("Result:", problem2())
	elapsed := time.Since(start)
	fmt.Printf("Execution time: %.6f seconds\n", elapsed.Seconds())
}
