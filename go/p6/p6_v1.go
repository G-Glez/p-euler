package main

import (
	"fmt"
	"time"
)

func problem6() int {
	const firstNNumbers int = 100

	const sumOfSquares int = (firstNNumbers * (firstNNumbers + 1) * (2*firstNNumbers + 1)) / 6
	const squareOfSum int = (firstNNumbers * (firstNNumbers + 1) / 2) * (firstNNumbers * (firstNNumbers + 1) / 2)

	return squareOfSum - sumOfSquares
}

func main() {
	start := time.Now()
	fmt.Println("Result:", problem6())
	elapsed := time.Since(start)
	fmt.Printf("Execution time: %.6f seconds\n", elapsed.Seconds())
}
