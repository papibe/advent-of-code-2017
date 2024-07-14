package main

import (
	"fmt"
	"math"
	"os"
	"regexp"
	"strconv"
	"strings"
)

const ALL = -1

func parse(filename string) []int {
	data, err := os.ReadFile(filename)

	if err != nil {
		panic("file error")
	}
	data_line := strings.Trim(string(data), "\n")
	re_space := regexp.MustCompile(`\s+`)

	instructions := []int{}
	for _, str_number := range re_space.Split(data_line, ALL) {
		number, _ := strconv.Atoi(str_number)
		instructions = append(instructions, number)
	}
	return instructions
}

func hash_memory(instructions []int) string {
	str_instructions := []string{}
	for _, number := range instructions {
		n_str := strconv.Itoa(number)
		str_instructions = append(str_instructions, n_str)
	}
	return strings.Join(str_instructions, "")
}

func rellocation(instructions []int) {
	// find max blocks
	max_blocks := math.MinInt
	max_index := 0

	for bank_index, nblocks := range instructions {
		if nblocks > max_blocks {
			max_blocks = nblocks
			max_index = bank_index
		}
	}

	// redistribution process
	n := len(instructions)
	instructions[max_index] = 0
	index := (max_index + 1) % n
	for i := 0; i < max_blocks; i++ {
		instructions[index] += 1
		index = (index + 1) % n
	}
}

func solve(instructions []int) int {
	cycles := 0
	seen := make(map[string]bool)
	current_state := hash_memory(instructions)

	_, has_seen := seen[current_state]

	for !has_seen {
		seen[current_state] = true
		rellocation(instructions)
		current_state = hash_memory(instructions)
		cycles++
		_, has_seen = seen[current_state]
	}

	return cycles
}

func solution(filename string) int {
	instructions := parse(filename)
	return solve(instructions)
}

func main() {
	fmt.Println(solution("./example.txt")) // 5
	fmt.Println(solution("./input.txt"))   // 14029
}
