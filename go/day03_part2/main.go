package main

import (
	"fmt"
)

var DIRECTIONS = [][2]int{{0, 1}, {-1, 0}, {0, -1}, {1, 0}}

var NEIGHBORS = [][2]int{{0, 1}, {-1, 0}, {0, -1}, {1, 0}, {-1, -1}, {-1, 1}, {1, -1}, {1, 1}}

type Coord struct {
	row int
	col int
}

type Grid map[Coord]int

func (g Grid) get_neighbors_value(row, col int) int {
	total := 0
	for _, coord := range NEIGHBORS {
		row_step, col_step := coord[0], coord[1]
		value, ok := g[Coord{row + row_step, col + col_step}]
		if ok {
			total += value
		}
	}
	return total
}

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

func solution(n int) int {
	grid := make(Grid)

	start_row := 0
	start_col := 0

	side_size := 1
	value := 1

	grid[Coord{0, 0}] = value

	for {
		side_size += 2

		for
	}
}

func main() {
	fmt.Println(solution(277678)) // 475
}
