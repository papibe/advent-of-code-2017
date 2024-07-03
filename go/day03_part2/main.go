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

// Iterator
// Rangefunc Experiment: https://go.dev/wiki/RangefuncExperiment
func next_position(row, col int) func(func(int, Coord) bool) {

	return func(yield func(int, Coord) bool) {
		index := 0
		steps := 1

		for {
			for i := 0; i < 2; i++ {
				for j := 0; j < steps; j++ {
					row += DIRECTIONS[index][0]
					col += DIRECTIONS[index][1]
					if !yield(0, Coord{row, col}) {
						return
					}
				}
				index = (index + 1) % len(DIRECTIONS)
			}
			steps += 1
		}
	}

}

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

func solution(n int) int {
	grid := make(Grid)

	start_row := 0
	start_col := 0

	grid[Coord{0, 0}] = 1

	for {
		for _, coord := range next_position(start_row, start_col) {
			row, col := coord.row, coord.col
			grid[coord] = grid.get_neighbors_value(row, col)

			if grid[coord] > n {
				return grid[coord]
			}

		}

	}
}

func main() {
	fmt.Println(solution(277678)) // 475
}
