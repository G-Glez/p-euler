package main

import (
	"fmt"
	"time"
)

func problem7() int {
	var isPrime = func (number int, primer_numbers []int) bool {
		for _, prime := range primer_numbers {
			if number%prime == 0 {
				return false
			}
		}
		return true
	}

	const n int = 10001

	primeNumbers := []int{2}

	primeCandidate := 3

	for len(primeNumbers) < n {
		if isPrime(primeCandidate, primeNumbers) {
			primeNumbers = append(primeNumbers, primeCandidate)
		}
		primeCandidate += 2
	}

	return primeNumbers[n-1]
}

func main() {
	start := time.Now()
	fmt.Println("Result:", problem7())
	elapsed := time.Since(start)
	fmt.Printf("Execution time: %.6f seconds\n", elapsed.Seconds())
}
