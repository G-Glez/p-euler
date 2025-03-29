package main

import (
	"fmt"
	"time"
)

func problem1() int {
	result := 0

	for i := range 1000 {
		if i%3 == 0 || i%5 == 0 {
			result += i
		}
	}
	return result
}

func main() {
	start := time.Now()
	fmt.Println("Result:", problem1())
	elapsed := time.Since(start)
	fmt.Printf("Execution time: %.6f seconds\n", elapsed.Seconds())
}
