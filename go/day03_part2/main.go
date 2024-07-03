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

// type PositionIterator struct {
// 	index int
// 	steps int
// 	row   int
// 	col   int
// }

// func (pi *PositionIterator) next_position() (int, int) {
// 	for {
// 		for i := 0; i < 2; i++ {
// 			for j := 0; j < pi.steps; j++ {
// 				pi.row += DIRECTIONS[pi.index][0]
// 				pi.col += DIRECTIONS[pi.index][1]
// 				return pi.row, pi.col
// 			}
// 			pi.index = (pi.index + 1) % len(DIRECTIONS)
// 		}
// 		pi.steps += 1
// 	}
// }

// https://go.dev/wiki/RangefuncExperiment
// https://makubob.medium.com/exploring-the-upcoming-go-generators-344b2fb98ff9

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
	// next_position := next_position_generator(start_row, start_col)

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
