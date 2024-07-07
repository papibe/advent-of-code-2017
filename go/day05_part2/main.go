package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func parse(filename string) []int {
	data, err := os.ReadFile(filename)

	if err != nil {
		panic("file error")
	}
	instructions := []int{}
	for _, str_number := range strings.Split(strings.Trim(string(data), "\n"), "\n") {
		number, _ := strconv.Atoi(str_number)
		instructions = append(instructions, number)
	}
	return instructions
}

func solve(instructions []int) int {
	pointer := 0
	min_pointer := 0
	max_pointer := len(instructions) - 1
	steps := 1

	for {
		jump := instructions[pointer]
		if jump >= 3 {
			instructions[pointer] -= 1
		} else {
			instructions[pointer] += 1
		}
		pointer += jump
		if pointer < min_pointer || pointer > max_pointer {
			return steps
		}
		steps += 1
	}
}

func solution(filename string) int {
	instructions := parse(filename)

	return solve(instructions)
}

func main() {
	fmt.Println(solution("./example.txt")) // 10
	fmt.Println(solution("./input.txt"))   // 28178177
}
