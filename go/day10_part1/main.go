package main

import (
	"fmt"
	"os"
	"strconv"
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

func parse(filename string) []int {
	data, err := os.ReadFile(filename)

	if err != nil {
		panic("file error")
	}
	str_numbers := strings.Split(strings.Trim(string(data), "\n"), ",")
	lengths := []int{}
	for _, str_number := range str_numbers {
		number, _ := strconv.Atoi(strings.Trim(str_number, " "))
		lengths = append(lengths, number)
	}
	return lengths
}

func solve(elements Elements, lengths []int) int {
	for _, length := range lengths {
		elements.apply(length)
	}
	return elements.top()
}

func solution(filename string, size int) int {
	lengths := parse(filename)
	elements := MakeElements(size)

	return solve(elements, lengths)
}

func main() {
	fmt.Println(solution("./example.txt", 5)) // 12
	fmt.Println(solution("./input.txt", 256)) // 40132
}
