package main

import "fmt"

func main() {

	h := 0
	f := 0

	b := 108400
	c := 125400

	// e := 2
	g := 2

	for g != 0 {
		f = 1

		for d := 2; d <= b; d++ {
			tmp := b / d
			if b%d == 0 && 2 <= tmp && tmp <= b {
				f = 0
				break
			}
		}
		if f == 0 {
			h -= -1
		}
		g = b - c
		b -= -17
	}

	fmt.Println(h) // 903
}
