package main

import (
	"fmt"
)

const GEN_A_FACTOR = 16807
const GEN_B_FACTOR = 48271
const DIVISOR = 2147483647
const MASK = 0xFFFF
const NUM_PAIRS = 40_000_000

func generator(previous_value, factor int) int {
	return (previous_value * factor) % DIVISOR
}

func solution(a_value, b_value, num_pars int) int {
	counter := 0

	for i := 0; i < num_pars; i++ {
		a_value = generator(a_value, GEN_A_FACTOR)
		b_value = generator(b_value, GEN_B_FACTOR)

		if (a_value & MASK) == (b_value & MASK) {
			counter++
		}
	}
	return counter
}

func main() {
	fmt.Println(solution(699, 124, NUM_PAIRS)) // 600
}
