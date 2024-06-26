package main

import (
	"fmt"
	"math"
	"os"
	"regexp"
	"strconv"
	"strings"
)

const ALL_SUBSTRINGS = -1

func parse(filename string) [][]int {
	data, err := os.ReadFile(filename)

	if err != nil {
		panic("file error")
	}
	content := strings.Split(strings.Trim(string(data), "\n"), "\n")

	re_split := regexp.MustCompile(`\s`)

	spreadsheet := [][]int{}
	for _, line := range content {
		numbers := re_split.Split(line, ALL_SUBSTRINGS)
		row := []int{}
		for _, n := range numbers {
			number, _ := strconv.Atoi(n)
			row = append(row, number)
		}
		spreadsheet = append(spreadsheet, row)
	}

	return spreadsheet
}

func solve(spreadsheet [][]int) int {
	checksum := 0

	for _, row := range spreadsheet {
		min_value := math.MaxInt
		max_value := math.MinInt
		for _, number := range row {
			min_value = min(min_value, number)
			max_value = max(max_value, number)
		}
		checksum += max_value - min_value
	}

	return checksum
}

func solution(filename string) int {
	spreadsheet := parse(filename)
	return solve(spreadsheet)
}

func main() {
	fmt.Println(solution("./example1.txt")) // 18
	fmt.Println(solution("./input.txt"))    // 39126
}
