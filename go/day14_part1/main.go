package main

import (
	"fmt"
)

var ONES = map[rune]int{
	'0': 0, // 0000
	'1': 1, // 0001
	'2': 1, // 0010
	'3': 2, // 0011
	'4': 1, // 0100
	'5': 2, // 0101
	'6': 2, // 0110
	'7': 3, // 0111
	'8': 1, // 1000
	'9': 2, // 1001
	'a': 2, // 1010
	'b': 3, // 1011
	'c': 2, // 1100
	'd': 3, // 1101
	'e': 3, // 1110
	'f': 4, // 1111
}

func solution(input string) int {
	used_squares := 0
	for row_number := 0; row_number < 128; row_number++ {
		row_input := fmt.Sprintf("%s-%d", input, row_number)
		row_hash := knot_hash(row_input, 256)
		for _, char := range row_hash {
			used_squares += ONES[char]
		}
	}
	return used_squares
}

func main() {
	fmt.Println(solution("flqrgnkx")) // 8108
	fmt.Println(solution("hxtvlmkl")) // 8214
}
