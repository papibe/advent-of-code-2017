package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

type TreeNode struct {
	name     string
	weight   int
	children []*TreeNode
}

func (t *TreeNode) add_child(node *TreeNode) {
	t.children = append(t.children, node)
}

func parse(filename string) *TreeNode {
	data, err := os.ReadFile(filename)

	if err != nil {
		panic("file error")
	}
	data_lines := strings.Split(strings.Trim(string(data), "\n"), "\n")

	programs := make(map[string]*TreeNode)
	re_line := regexp.MustCompile(`^(\w+) \((\d+)\)`)

	// first pass: build main nodes
	for _, line := range data_lines {
		match := re_line.FindStringSubmatch(line)
		name := match[1]
		weight, _ := strconv.Atoi(match[2])

		programs[name] = &TreeNode{name, weight, []*TreeNode{}}
	}

	candidates_for_root := make(map[string]bool)
	for program_name, _ := range programs {
		candidates_for_root[program_name] = true
	}

	// second pass: add child nodes
	for _, line := range data_lines {
		if !strings.Contains(line, "->") {
			continue
		}
		match := re_line.FindStringSubmatch(line)
		name := match[1]

		upper_programs := strings.Split(strings.Split(line, " -> ")[1], ", ")
		for _, uprogram := range upper_programs {
			node := programs[name]
			node.add_child(programs[uprogram])
			delete(candidates_for_root, uprogram)
		}

	}
	if len(candidates_for_root) != 1 {
		panic("more than one root?")
	}

	for root, _ := range candidates_for_root {
		return programs[root]
	}
	return &TreeNode{"", 0, []*TreeNode{}}
}

func get_unbalance(children_weights map[int][]*TreeNode) (int, int, *TreeNode) {
	var unbalance_node *TreeNode
	var unbalance_weight int
	var balance_weight int

	for weight, nodes := range children_weights {
		if len(nodes) == 1 {
			unbalance_node = nodes[0]
			unbalance_weight = weight
		} else {
			balance_weight = weight
		}
	}
	return balance_weight, unbalance_weight, unbalance_node
}

func balance_weight(node *TreeNode) (int, int) {
	if len(node.children) == 0 {
		return node.weight, 0
	}

	children_weights := make(map[int][]*TreeNode)
	for _, child := range node.children {
		weight, balance := balance_weight(child)

		// shortcut: once balance is discovered stop calculated all weights
		if balance > 0 {
			return weight, balance
		}

		_, seen := children_weights[weight]
		if seen {
			children_weights[weight] = append(children_weights[weight], child)
		} else {
			children_weights[weight] = []*TreeNode{child}
		}
	}
	// no balance problems
	if len(children_weights) == 1 {
		var unique_weight int
		for uw, _ := range children_weights {
			unique_weight = uw
		}
		total_children_weight := unique_weight * len(node.children)
		return node.weight + total_children_weight, 0
	}

	// balance needed
	balanced_weigth, unbalanced_weigth, unbalanced_node := get_unbalance(children_weights)
	diff_weight := balanced_weigth - unbalanced_weigth
	total_children_weight := 0
	for weight, _ := range children_weights {
		total_children_weight += weight
	}
	return total_children_weight, unbalanced_node.weight + diff_weight
}

func solution(filename string) int {
	root := parse(filename)
	_, balance := balance_weight(root)
	return balance
}

func main() {
	fmt.Println(solution("./example.txt")) // 60
	fmt.Println(solution("./input.txt"))   // 256
}
