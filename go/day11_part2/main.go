package main

import (
	"fmt"
	"os"
	"strings"
)

type HexCoord struct {
	q int
	r int
	s int
}

var DISTANCE = map[string]HexCoord{
	"n":  {0, 1, -1},
	"ne": {1, 0, -1},
	"se": {1, -1, 0},
	"s":  {0, -1, 1},
	"sw": {-1, 0, 1},
	"nw": {-1, 1, 0},
}

func abs(a int) int {
	if a > 0 {
		return a
	}
	return -a
}

func parse(filename string) []string {
	data, err := os.ReadFile(filename)

	if err != nil {
		panic("file error")
	}
	return strings.Split(strings.Trim(string(data), "\n"), ",")
}

func solve(directions []string) int {
	current := HexCoord{0, 0, 0}
	max_distance := 0

	for _, dir := range directions {
		delta := DISTANCE[dir]
		current = HexCoord{
			current.q + delta.q,
			current.r + delta.r,
			current.s + delta.s,
		}
		max_distance = max(
			max_distance,
			max(abs(current.q), abs(current.r), abs(current.s)),
		)
	}
	return max_distance
}

func solution(filename string) int {
	directions := parse(filename)
	return solve(directions)
}

func main() {
	fmt.Println(solution("./input.txt")) // 1469
}
