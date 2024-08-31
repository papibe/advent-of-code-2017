package main

import (
	"fmt"
)

const GEN_A_FACTOR = 16807
const GEN_B_FACTOR = 48271
const DIVISOR = 2147483647
const MASK = 0xFFFF
const NUM_PAIRS = 5_000_000

type Generator struct {
	value    int
	factor   int
	multiple int
}

func (g *Generator) next() int {
	for {
		g.value = (g.value * g.factor) % DIVISOR
		if (g.value % g.multiple) == 0 {
			return g.value
		}
	}
}

func solve(genA, genB Generator, num_pars int) int {
	counter := 0

	for i := 0; i < num_pars; i++ {
		if (genA.next() & MASK) == (genB.next() & MASK) {
			counter++
		}
	}
	return counter
}

func solution(a_value, b_value, num_pars int) int {
	genA := Generator{a_value, GEN_A_FACTOR, 4}
	genB := Generator{b_value, GEN_B_FACTOR, 8}

	return solve(genA, genB, num_pars)
}

func main() {
	fmt.Println(solution(699, 124, NUM_PAIRS)) // 313
}
