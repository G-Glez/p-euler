package main

import (
	"fmt"
	"strconv"
	"time"
)

func problem4() int {
	var isPalindrome = func(n int) bool {
		nAsString := strconv.Itoa(n)
		for i, j := 0, len(strconv.Itoa(n))-1; i < j; i, j = i+1, j-1 {
			if nAsString[i] != nAsString[j] {
				return false
			}
		}
		return true
	}

	const upperBound int = 999
	const lowerBound int = 99

	palindrome := 0

	multiplicand := upperBound

	for multiplicand > lowerBound && multiplicand*upperBound > palindrome {
		for multiplier := upperBound; multiplier > lowerBound; multiplier-- {
			product := multiplicand * multiplier
			if product > palindrome && isPalindrome(product) {
				palindrome = product
			}
		}
		multiplicand--
	}

	return palindrome
}

func main() {
	start := time.Now()
	fmt.Println("Result:", problem4())
	elapsed := time.Since(start)
	fmt.Printf("Execution time: %.6f seconds\n", elapsed.Seconds())
}
