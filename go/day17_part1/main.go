package main

import (
	"fmt"
)

type Node struct {
	value int
	next  *Node
	prev  *Node
}

type Buffer struct {
	head     *Node
	size     int
	spinlock int
}

func NewBuffer(spinlock int) Buffer {
	node := Node{spinlock, nil, nil}
	node.next = &node
	node.prev = &node

	return Buffer{&node, 1, spinlock}
}

func (b *Buffer) insert(value int) {
	// round up spinlock
	insert_position := b.spinlock % b.size

	// find where to insert
	current := b.head
	for i := 0; i < insert_position; i++ {
		current = current.next
	}

	node := &Node{value, nil, nil}

	// insert
	next := current.next
	current.next = node
	node.prev = current
	node.next = next
	next.prev = node

	b.head = node
	b.size++
}

func solution(spinlock int) int {
	buffer := NewBuffer(spinlock)

	for value := 1; value <= 2017; value++ {
		buffer.insert(value)
	}
	return buffer.head.next.value
}

func main() {
	fmt.Println(solution(3))   // 638
	fmt.Println(solution(371)) // 1311
}
