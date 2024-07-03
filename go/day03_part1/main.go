package main

import (
	"fmt"
	"math"
)

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

func solution(n int) int {
	aprox_box_size := int(math.Ceil(math.Sqrt(float64(n))))

	var box_side int
	if aprox_box_size%2 == 0 {
		box_side = aprox_box_size + 1
	} else {
		box_side = aprox_box_size
	}
	lower_right_corner := box_side * box_side

	steps_to_border := (box_side+1)/2 - 1

	bottom := lower_right_corner - box_side/2
	left := lower_right_corner - 3*(box_side/2)
	top := lower_right_corner - 5*(box_side/2)
	right := lower_right_corner - 7*(box_side/2)

	extra_steps := min(
		abs(bottom-n),
		abs(left-n),
		abs(top-n),
		abs(right-n),
	)
	return steps_to_border + extra_steps
}

func main() {
	fmt.Println(solution(277678)) // 475
}
