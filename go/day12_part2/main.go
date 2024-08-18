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

func find(p int, parents []int) int {
	for p != parents[p] {
		p = parents[p]
	}
	return p
}

func union(p, q int, parents []int) {
	root_p, root_q := find(p, parents), find(q, parents)
	parents[root_p] = root_q
}

func solve(pipes AdjacencyList) int {

	parents := []int{}
	for i := 0; i < len(pipes); i++ {
		parents = append(parents, i)
	}

	for node, neighbors := range pipes {
		for neighbor := range neighbors {
			union(neighbor, node, parents)
		}
	}

	collection_of_parents := make(map[int]bool)
	for node, _ := range pipes {
		collection_of_parents[find(node, parents)] = true
	}

	return len(collection_of_parents)
}

func solution(filename string) int {
	pipes := parse(filename)
	return solve(pipes)
}

func main() {
	fmt.Println(solution("./example.txt")) // 2
	fmt.Println(solution("./input.txt"))   // 209
}
