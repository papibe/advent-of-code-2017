package main

import (
	"fmt"
	"strings"
)

var ONES = map[rune]string{
	'0': "0000",
	'1': "0001",
	'2': "0010",
	'3': "0011",
	'4': "0100",
	'5': "0101",
	'6': "0110",
	'7': "0111",
	'8': "1000",
	'9': "1001",
	'a': "1010",
	'b': "1011",
	'c': "1100",
	'd': "1101",
	'e': "1110",
	'f': "1111",
}

type Position struct {
	row int
	col int
}

var STEPS = []Position{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}

type Deque []Position

func (q *Deque) append(dk Position) {
	(*q) = append((*q), dk)
}

func (q Deque) isEmpty() bool {
	return len(q) == 0
}

func (q *Deque) popleft() Position {
	item := (*q)[0]
	(*q) = (*q)[1:]
	return item
}

func solution(input string) int {
	grid := []string{}
	for row_number := 0; row_number < 128; row_number++ {
		row_input := fmt.Sprintf("%s-%d", input, row_number)
		row_hash := knot_hash(row_input, 256)

		grid_row := []string{}
		for _, char := range row_hash {
			grid_row = append(grid_row, ONES[char])
		}
		grid = append(grid, strings.Join(grid_row, ""))
	}

	regions := 0
	visited := make(map[Position]bool)

	for row := 0; row < 128; row++ {
		for col := 0; col < 128; col++ {

			_, is_visited := visited[Position{row, col}]

			if grid[row][col] == '0' || is_visited {
				continue
			}

			// BFS
			regions++
			start := Position{row, col}
			visited[start] = true
			queue := Deque{}
			queue.append(start)

			for !queue.isEmpty() {
				current := queue.popleft()

				for _, step := range STEPS {
					new_row := current.row + step.row
					new_col := current.col + step.col

					if 0 <= new_row && new_row < 128 && 0 <= new_col && new_col < 128 {
						if grid[new_row][new_col] == '0' {
							continue
						}
						new_position := Position{new_row, new_col}
						_, is_visited := visited[new_position]
						if !is_visited {
							queue.append(new_position)
							visited[new_position] = true
						}

					}
				}
			}
		}
	}

	return regions
}

func main() {
	fmt.Println(solution("flqrgnkx")) // 1242
	fmt.Println(solution("hxtvlmkl")) // 1093
}
