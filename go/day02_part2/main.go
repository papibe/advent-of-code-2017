package main

import (
	"fmt"
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
		n := len(row)
		for i := 0; i < n; i++ {
			for j := i + 1; j < n; j++ {
				if row[i]%row[j] == 0 {
					checksum += row[i] / row[j]
				} else if row[j]%row[i] == 0 {
					checksum += row[j] / row[i]
				}
			}
		}
	}

	return checksum
}

func solution(filename string) int {
	spreadsheet := parse(filename)
	return solve(spreadsheet)
}

func main() {
	fmt.Println(solution("./example2.txt")) // 9
	fmt.Println(solution("./input.txt"))    // 258
}
