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
	zero     *Node
}

func NewBuffer(spinlock int) Buffer {
	node := Node{spinlock, nil, nil}
	node.next = &node
	node.prev = &node

	return Buffer{&node, 1, spinlock, &node}
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

	for value := 1; value <= 50000000; value++ {
		buffer.insert(value)
	}
	return buffer.zero.next.value
}

func main() {
	// it takes 2m26s
	fmt.Println(solution(371)) // 39170601
}
