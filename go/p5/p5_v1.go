package main

import (
	"fmt"
	"math"
	"time"
)

func problem5() int {
	const to int = 20

	factors := make([]int, to)

	for i := 1; i <= to; i++ {
		counter := 2
		currentFactors := make([]int, i)

		num := i

		for num != 1 {
			if num%counter == 0 {
				num /= counter
				currentFactors[counter-1] += 1
			} else {
				counter += 1 + counter%2
			}

		}

		for j := range currentFactors {
			if currentFactors[j] > factors[j] {
				factors[j] = currentFactors[j]
			}
		}
	}

	var result int = 1
	
	for i, factor := range factors {
		result *= int(math.Pow(float64(i+1), float64(factor)))
	}

	return result
}

func main() {
	start := time.Now()
	fmt.Println("Result:", problem5())
	elapsed := time.Since(start)
	fmt.Printf("Execution time: %.6f seconds\n", elapsed.Seconds())
}
