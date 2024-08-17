package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

type HexCoord struct {
	q int
	r int
	s int
}

type Deque []int

func (q *Deque) append(dk int) {
	(*q) = append((*q), dk)
}

func (q Deque) isEmpty() bool {
	return len(q) == 0
}

func (q *Deque) popleft() int {
	item := (*q)[0]
	(*q) = (*q)[1:]
	return item
}

type AdjacencyList map[int]map[int]bool

func abs(a int) int {
	if a > 0 {
		return a
	}
	return -a
}

func parse(filename string) AdjacencyList {
	data, err := os.ReadFile(filename)

	if err != nil {
		panic("file error")
	}
	lines := strings.Split(strings.Trim(string(data), "\n"), "\n")

	re := regexp.MustCompile(`(?P<node>\d+) <-> (?P<node_list>.*)`)
	adjacency_list := make(AdjacencyList)

	for _, line := range lines {
		matches := re.FindStringSubmatch(line)
		node, _ := strconv.Atoi(matches[1])
		node_list_str := matches[2]
		adjacency_list[node] = make(map[int]bool)
		for _, n_str := range strings.Split(node_list_str, ", ") {
			n, _ := strconv.Atoi(n_str)
			adjacency_list[node][n] = true
		}
	}
	return adjacency_list
}

func solve(pipes AdjacencyList) int {
	connections_to_zero := 0

	for node, _ := range pipes {
		if node == 0 {
			connections_to_zero++
			continue
		}

		visited := make(map[int]bool)
		queue := Deque{}
		queue.append(node)
		visited[node] = true

		for !queue.isEmpty() {
			current := queue.popleft()
			if current == 0 {
				connections_to_zero++
				break
			}

			for neighbor, _ := range pipes[current] {
				_, is_visited := visited[neighbor]
				if !is_visited {
					visited[neighbor] = true
					queue.append(neighbor)
				}
			}
		}
	}
	return connections_to_zero
}

func solution(filename string) int {
	pipes := parse(filename)
	return solve(pipes)
}

func main() {
	fmt.Println(solution("./example.txt")) // 6
	fmt.Println(solution("./input.txt"))   // 128
}
