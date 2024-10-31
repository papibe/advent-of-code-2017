package main

import (
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

type Component struct {
	port1 int
	port2 int
}

func (c Component) get_value() int {
	return c.port1 + c.port2
}

type Bridge struct {
	bridge []Component
}

func (b *Bridge) append(c Component) {
	b.bridge = append(b.bridge, c)
}

func (b *Bridge) pop() {
	b.bridge = b.bridge[:len(b.bridge)-1]
}

func (b Bridge) get_strength() int {
	strength := 0
	for _, component := range b.bridge {
		strength += component.get_value()
	}
	return strength
}

func parse(filename string) map[int]map[Component]bool {
	data, err := os.ReadFile(filename)
	if err != nil {
		panic("Input file not found!")
	}

	lines := strings.Split((strings.Trim(string(data), "\n")), "\n")

	comp_map := make(map[int]map[Component]bool)

	for _, line := range lines {
		ports := strings.Split(line, "/")
		port1, _ := strconv.Atoi(ports[0])
		port2, _ := strconv.Atoi(ports[1])

		component := Component{port1, port2}

		_, ok := comp_map[port1]
		if !ok {
			comp_map[port1] = make(map[Component]bool)
		}
		comp_map[port1][component] = true

		_, ok = comp_map[port2]
		if !ok {
			comp_map[port2] = make(map[Component]bool)
		}
		comp_map[port2][component] = true
	}
	return comp_map
}

func copy_components(cmap map[Component]bool) map[Component]bool {
	new_copy := make(map[Component]bool)
	for k, v := range cmap {
		new_copy[k] = v
	}
	return new_copy
}

func solve(bridge Bridge, top int, comp_map map[int]map[Component]bool) int {
	_, top_in_cmap := comp_map[top]

	// edge condition
	if len(comp_map) == 0 || !top_in_cmap || len(comp_map[top]) == 0 {
		return bridge.get_strength()
	}

	max_strengths := math.MinInt
	matching_components := copy_components(comp_map[top])

	// add component to bridge
	for component, _ := range matching_components {
		bridge.append(component)
		var new_top int
		if top == component.port2 {
			new_top = component.port1
		} else {
			new_top = component.port2
		}
		delete(comp_map[top], component)

		if top != new_top {
			delete(comp_map[new_top], component)
		}
		max_strengths = max(max_strengths, solve(bridge, new_top, comp_map))

		// backtrack
		bridge.pop()
		comp_map[top][component] = true
		comp_map[new_top][component] = true
	}
	return max_strengths
}

func solution(filename string) int {
	comp_map := parse(filename)

	pit := Component{0, 0}
	bridge := Bridge{[]Component{}}
	bridge.append(pit)
	top := 0
	return solve(bridge, top, comp_map)
}

func main() {
	fmt.Println(solution("./example.txt")) // 31
	fmt.Println(solution("./input.txt"))   // 1940
}
