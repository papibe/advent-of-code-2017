package main

import (
	"fmt"
	"os"
	"strings"
)

const INFECTED_NODE = '#'

type Node struct {
	row int
	col int
}

type Cluster map[Node]bool

func (c *Cluster) add(n Node) {
	(*c)[n] = true
}

func (c *Cluster) remove(n Node) {
	delete((*c), n)
}

func (c *Cluster) contains(n Node) bool {
	_, ok := (*c)[n]
	return ok
}

type Carrier struct {
	row int
	col int
	dir Node
}

func (n Carrier) position() Node {
	return Node{n.row, n.col}
}

func (n *Carrier) turn_right() {
	n.dir = Node{n.dir.col, -n.dir.row}
}

func (n *Carrier) turn_leftt() {
	n.dir = Node{-n.dir.col, n.dir.row}
}

func (n *Carrier) move() {
	n.row += n.dir.row
	n.col += n.dir.col
}

func parse(filename string) (Carrier, Cluster) {
	data, err := os.ReadFile(filename)
	if err != nil {
		panic("Input file not found!")
	}
	lines := strings.Split((strings.Trim(string(data), "\n")), "\n")

	cluster := make(Cluster)

	rows := len(lines)
	cols := len(lines[0])

	for row := 0; row < rows; row++ {
		for col := 0; col < cols; col++ {
			if lines[row][col] == INFECTED_NODE {
				cluster.add(Node{row, col})
			}
		}
	}
	carrier := Carrier{rows / 2, cols / 2, Node{-1, 0}}

	return carrier, cluster
}

func solve(carrier Carrier, cluster Cluster, bursts int) int {
	infections := 0

	for range bursts {
		position := carrier.position()

		// determine turn
		if cluster.contains(position) {
			carrier.turn_right()
		} else {
			carrier.turn_leftt()
		}

		// determine infection
		if !cluster.contains(position) {
			infections++
			cluster.add(position)
		} else {
			cluster.remove(position)
		}

		// actual move
		carrier.move()
	}
	return infections
}

func solution(filename string, bursts int) int {
	carrier, cluster := parse(filename)

	return solve(carrier, cluster, bursts)
}

func main() {
	fmt.Println(solution("./input.txt", 10_000)) // 5575
}
