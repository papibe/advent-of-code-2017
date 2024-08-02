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

func garbage(data string, index int) (int, int) {
	garbage_counter := 0
	for {
		if data[index] == '!' {
			index += 2
		} else if data[index] == '>' {
			return index, garbage_counter
		} else {
			garbage_counter++
			index++
		}
	}
}

func parse_stream(data string) (int, int) {
	score := 0
	index := 0
	level := 0
	total_garbage := 0
	var garbage_counter int

	for index < len(data) {
		if data[index] == '{' {
			level++
		} else if data[index] == '<' {
			index, garbage_counter = garbage(data, index+1)
			total_garbage += garbage_counter
		} else if data[index] == '}' {
			score += level
			level--
		}
		index++
	}
	return score, total_garbage
}

func solution(filename string) (int, int) {
	data := parse(filename)
	return parse_stream(data)
}

func main() {
	solution1, solution2 := solution("./input.txt")
	fmt.Println("Part1:", solution1) // 16869
	fmt.Println("Part1:", solution2) // 7284
}
