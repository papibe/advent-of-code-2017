package main

import (
	"fmt"
	"strings"
)

type Elements struct {
	size             int
	skip_size        int
	current_position int
	elements         []int
	next             []int
	prev             []int
}

func mod(a, b int) int {
	return (a%b + b) % b
}

func MakeElements(size int) Elements {
	elements := []int{}
	next := []int{}
	prev := []int{}

	for i := 0; i < size; i++ {
		elements = append(elements, i)
		next = append(next, mod(i+1, size))
		prev = append(prev, mod(i-1, size))
	}
	return Elements{size, 0, 0, elements, next, prev}
}

func (e *Elements) apply(length int) {
	current_index := e.current_position
	for i := 0; i < length-1; i++ {
		current_index = e.next[current_index]
	}

	head_index := e.current_position
	tail_index := current_index

	for head_index != tail_index && e.prev[head_index] != tail_index {
		value := e.elements[head_index]

		e.elements[head_index] = e.elements[tail_index]
		e.elements[tail_index] = value

		head_index = e.next[head_index]
		tail_index = e.prev[tail_index]
	}

	current_index = e.current_position
	for i := 0; i < length+e.skip_size; i++ {
		current_index = e.next[current_index]
	}

	e.current_position = current_index
	e.skip_size += 1
}

func (e Elements) top() int {
	return e.elements[0] * e.elements[e.next[0]]
}

func get_lengths(data string) []int {
	sequence := []int{}
	for _, char := range data {
		sequence = append(sequence, int(char))
	}
	sequence = append(sequence, []int{17, 31, 73, 47, 23}...)
	return sequence
}

func knot_hash(input string, size int) string {
	lengths := get_lengths(input)
	e := MakeElements(size)

	for i := 0; i < 64; i++ {
		for _, length := range lengths {
			e.apply(length)
		}
	}
	dense_hash := []int{}
	current_index := 0
	for i := 0; i < 16; i++ {
		xor := 0
		for j := 0; j < 16; j++ {
			xor ^= e.elements[current_index]
			current_index = e.next[current_index]
		}
		dense_hash = append(dense_hash, xor)
	}

	output := []string{}
	for _, n := range dense_hash {
		output = append(output, fmt.Sprintf("%02x", n))
	}

	return strings.Join(output, "")
}
