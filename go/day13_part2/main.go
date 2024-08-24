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

func pass_through_firewall(delay int, firewall map[int]int) bool {
	position := 0
	visited := make(map[int]bool)

	for len(visited) < len(firewall) {
		range_, is_in_firewall := firewall[position]
		if is_in_firewall {
			depth := position
			visited[depth] = true

			if is_at_top(position+delay, range_) {
				return false
			}
		}
		position++
	}
	return true
}

func solve(firewall map[int]int) int {
	delay := 0
	for {
		if pass_through_firewall(delay, firewall) {
			return delay
		}
		delay++
	}
}

func solution(filename string) int {
	firewall := parse(filename)
	return solve(firewall)
}

func main() {
	fmt.Println(solution("./example.txt")) // 10
	fmt.Println(solution("./input.txt"))   // 3966414
}
