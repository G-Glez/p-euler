package main

import (
	"fmt"
	"time"
)

func problem3() int {
	value := 600851475143
	largestPrimeFactor := 0
	nextPossibleFactor := 2

	for value != 1 {
		if value%nextPossibleFactor == 0 {
			largestPrimeFactor = nextPossibleFactor
			value /= nextPossibleFactor
		} else {
			nextPossibleFactor += 1 + nextPossibleFactor%2
		}
	}

	return largestPrimeFactor
}

func main() {
	start := time.Now()
	fmt.Println("Result:", problem3())
	elapsed := time.Since(start)
	fmt.Printf("Execution time: %.6f seconds\n", elapsed.Seconds())
}
