package main

import (
	"fmt"
	"os"
	"strings"
)

type Art [][]string

type Rules map[string]string

var INITIAL_ART = Art{
	{".", "#", "."},
	{".", ".", "#"},
	{"#", "#", "#"},
}

func parse(filename string) Rules {
	data, err := os.ReadFile(filename)
	if err != nil {
		panic("Input file not found!")
	}
	lines := strings.Split((strings.Trim(string(data), "\n")), "\n")

	rules := Rules{}

	for _, line := range lines {
		line_split := strings.Split(line, " => ")
		rule, transformation := line_split[0], line_split[1]
		rules[rule] = transformation
	}
	return rules
}

func rot90(art Art) Art {
	n := len(art)
	rot := make(Art, n)
	for i := range n {
		rot[i] = make([]string, n)
		for j := range n {
			rot[i][j] = art[n-j-1][i]
		}
	}
	return rot
}

func hflip(art Art) Art {
	n := len(art)
	flip := make(Art, n)
	for i := range n {
		flip[i] = make([]string, n)
		for j := range n {
			flip[i][j] = art[n-i-1][j]
		}
	}
	return flip
}

func copy(art Art) Art {
	n := len(art)
	tmp := make(Art, n)
	for i := range n {
		tmp[i] = make([]string, n)
		for j := range n {
			tmp[i][j] = art[i][j]
		}
	}
	return tmp

}

func get_transformations(art_ Art) []Art {
	art := copy(art_)
	transformations := []Art{art}

	// "90", "180", "270"
	for range 3 {
		art = rot90(art)
		transformations = append(transformations, art)
	}
	art = rot90(art)
	art = hflip(art)
	transformations = append(transformations, art)

	// "90f", "180f", "270f"
	for range 3 {
		art = rot90(art)
		transformations = append(transformations, art)
	}

	return transformations
}

func stringify(art Art) string {
	output := []string{}
	for _, row := range art {
		output = append(output, strings.Join(row, ""))
	}
	return strings.Join(output, "/")
}

func get_divisions(art Art, number int) []Art {
	size := len(art)
	n_divisions := size / number
	divisions := []Art{}

	for base_row := range n_divisions {

		for base_col := range n_divisions {
			start_row := base_row * number
			start_col := base_col * number

			division := Art{}

			for row := start_row; row < start_row+number; row++ {
				new_row := []string{}

				for col := start_col; col < start_col+number; col++ {
					new_row = append(new_row, art[row][col])
				}
				division = append(division, new_row)
			}
			divisions = append(divisions, division)
		}
	}
	return divisions
}

func enhancement_rule(art Art, rules Rules, number int) Art {

	divisions := get_divisions(art, number)

	transformations := []string{}
	for _, division := range divisions {
		rotations := get_transformations(division)

		for _, rotation := range rotations {
			string_rep := stringify(rotation)

			trans, in_rules := rules[string_rep]
			if in_rules {
				transformations = append(transformations, trans)
				break
			}
		}
	}

	size := len(art)
	n_divisions := size / number

	// join pieces
	new_size := (number + 1) * n_divisions
	art = make(Art, new_size)
	for row := range new_size {
		art[row] = make([]string, new_size)
	}
	transformation_index := 0

	for base_row := range n_divisions {
		for base_col := range n_divisions {
			start_row := base_row * (number + 1)
			start_col := base_col * (number + 1)

			transformation := transformations[transformation_index]
			transformation_index++
			trans_index := 0
			for row := start_row; row < start_row+number+1; row++ {

				for col := start_col; col < start_col+number+1; col++ {
					art[row][col] = string(transformation[trans_index])
					trans_index++
				}
				trans_index++ // skip "/"
			}

		}
	}
	return art
}

func count_pixels(art Art) int {
	counter := 0
	for _, row := range art {
		for _, char := range row {
			if char == "#" {
				counter++
			}
		}
	}
	return counter
}

func solve(art Art, interactions int, rules Rules) int {

	for range interactions {
		size := len(art)

		if size%2 == 0 {
			art = enhancement_rule(art, rules, 2)
		} else {
			art = enhancement_rule(art, rules, 3)
		}
	}

	return count_pixels(art)
}

func solution(filename string, interactions int) int {
	art := INITIAL_ART
	rules := parse(filename)

	return solve(art, interactions, rules)
}

func main() {
	fmt.Println(solution("./example.txt", 2)) // 12
	fmt.Println(solution("./input.txt", 5))   // 123
}
