package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func parse(filename string) map[int]int {
	data, err := os.ReadFile(filename)

	if err != nil {
		panic("file error")
	}
	lines := strings.Split(strings.Trim(string(data), "\n"), "\n")

	re := regexp.MustCompile(`(?P<depth>\d+): (?P<range>\d+)`)
	firewall := make(map[int]int)

	for _, line := range lines {
		matches := re.FindStringSubmatch(line)
		depth, _ := strconv.Atoi(matches[1])
		range_, _ := strconv.Atoi(matches[2])
		firewall[depth] = range_
	}
	return firewall
}

func is_at_top(picosecond int, scanner_range int) bool {
	return (picosecond % (2*scanner_range - 2)) == 0
}

func solve(firewall map[int]int) int {
	severity := 0
	picosecond := 0 // also position
	visited := make(map[int]bool)

	for len(visited) < len(firewall) {
		range_, is_in_firewall := firewall[picosecond]
		if is_in_firewall {
			depth := picosecond
			visited[depth] = true

			if is_at_top(picosecond, range_) {
				severity += depth * range_
			}
		}
		picosecond++
	}
	return severity
}

func solution(filename string) int {
	firewall := parse(filename)
	return solve(firewall)
}

func main() {
	fmt.Println(solution("./example.txt")) // 24
	fmt.Println(solution("./input.txt"))   // 1900
}
