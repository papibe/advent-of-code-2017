package main

import (
	"fmt"
	"os"
	"strings"
)

func parse(filename string) string {
	data, err := os.ReadFile(filename)

	if err != nil {
		panic("file error")
	}

	return strings.Trim(string(data), "\n")
}

func solve(data string) int {
	n := len(data)
	half_distance := n / 2
	total_sum := 0

	for i := 0; i < n; i++ {
		if data[i] == data[(i+half_distance)%n] {
			total_sum += int(data[i]) - '0'
		}
	}
	return total_sum
}

func solution(filename string) int {
	data := parse(filename)
	return solve(data)
}

func main() {
	fmt.Println(solution("./input.txt")) // 950
}
