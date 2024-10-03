package main

import (
	"fmt"
	"os"
	"regexp"
	"strings"
)

var DIRECTIONS = [][2]int{{0, 1}, {-1, 0}, {0, -1}, {1, 0}}

type Coord struct {
	row int
	col int
}

type Diagram []string

func parse(filename string) Diagram {
	data, err := os.ReadFile(filename)
	if err != nil {
		panic("Input file not found!")
	}
	return strings.Split((strings.Trim(string(data), "\n")), "\n")
}

func is_alpha(word string) bool {
	return regexp.MustCompile(`^[a-zA-Z]*$`).MatchString(word)
}

func inbound(row, col int, diagram Diagram) bool {
	is_in_row_range := (0 <= row && row < len(diagram))
	is_in_col_range := (0 <= col && row < len(diagram[0]))

	return is_in_row_range && is_in_col_range
}

func traverse(row, col int, diagram Diagram) func(func(int, Coord) bool) {

	return func(yield func(int, Coord) bool) {
		dir_row := 1
		dir_col := 0

		prev_row := row
		prev_col := col

		var next_row int
		var next_col int

		for diagram[row][col] != ' ' {

			if diagram[row][col] != '+' {
				next_row = row + dir_row
				next_col = col + dir_col

				if !yield(0, Coord{next_row, next_col}) {
					return
				}
				prev_row, prev_col = row, col
				row, col = next_row, next_col
				continue
			}

			for _, step := range DIRECTIONS {
				neighbor_row := row + step[0]
				neighbor_col := col + step[1]

				is_previous := (neighbor_row == prev_row) && (neighbor_col == prev_col)
				is_inbound := inbound(neighbor_row, neighbor_col, diagram)
				is_blank := diagram[neighbor_row][neighbor_col] == ' '

				if is_previous || !is_inbound || is_blank {
					continue
				}

				if !yield(0, Coord{neighbor_row, neighbor_col}) {
					return
				}
				dir_row = neighbor_row - next_row
				dir_col = neighbor_col - next_col

				prev_row, prev_col = row, col
				row, col = neighbor_row, neighbor_col
				break
			}
		}
	}
}

func solve(diagram Diagram) int {
	// find start position
	var start_col int
	for col, char := range diagram[0] {
		if char != ' ' {
			start_col = col
			break
		}
	}

	steps := 0

	// traverse the diagram
	for _, coord := range traverse(0, start_col, diagram) {
		_ = coord // dumb go
		steps++
	}

	return steps
}

func solution(filename string) int {
	diagram := parse(filename)
	return solve(diagram)
}

func main() {
	fmt.Println(solution("./example.txt")) // 38
	fmt.Println(solution("./input.txt"))   // 16312
}
