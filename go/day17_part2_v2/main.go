package main

import (
	"fmt"
)

type Buffer struct {
	head_position int
	size          int
	spinlock      int
	zero_postion  int
	next_to_zero  int
}

func (b *Buffer) insert(value int) {
	// round up spinlock
	insert_position := b.spinlock % b.size

	if insert_position == b.zero_postion {
		b.next_to_zero = value
		b.zero_postion = b.size

	} else if insert_position < b.zero_postion {
		b.zero_postion -= insert_position

	} else if insert_position > b.zero_postion {
		b.zero_postion += b.size - insert_position
	}
	b.size++
}

func solution(spinlock int) int {
	buffer := Buffer{0, 1, spinlock, 0, 0}

	for value := 1; value <= 50000000; value++ {
		buffer.insert(value)
	}
	return buffer.next_to_zero
}

func main() {
	// it takes 140ms
	fmt.Println(solution(371)) // 39170601
}
