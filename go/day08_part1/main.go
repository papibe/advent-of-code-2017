package main

import (
	"fmt"
	"math"
	"os"
	"regexp"
	"strconv"
	"strings"
)

type Instruction struct {
	register1  string
	operation  string
	number1    int
	register2  string
	comparison string
	number2    int
}

type Computer struct {
	registers map[string]int
}

func NewComputer() Computer {
	return Computer{make(map[string]int)}
}

func (c Computer) add_register(register string) {
	c.registers[register] = 0
}

func (c Computer) compare(register, op string, n int) bool {
	var comparisons = map[string]func(int, int) bool{
		">":  func(r, n int) bool { return r > n },
		"<":  func(r, n int) bool { return r < n },
		"<=": func(r, n int) bool { return r <= n },
		">=": func(r, n int) bool { return r >= n },
		"==": func(r, n int) bool { return r == n },
		"!=": func(r, n int) bool { return r != n },
	}
	return comparisons[op](c.registers[register], n)
}

func (c Computer) operation(register, op string, n int) {
	var operations = map[string]func(int, int) int{
		"inc": func(r, n int) int { return r + n },
		"dec": func(r, n int) int { return r - n },
	}
	c.registers[register] = operations[op](c.registers[register], n)
}

func (c Computer) get_max_register() int {
	max_reg := math.MinInt
	for _, value := range c.registers {
		max_reg = max(max_reg, value)
	}
	return max_reg
}

func parse(filename string) (Computer, []Instruction) {
	data, err := os.ReadFile(filename)

	if err != nil {
		panic("file error")
	}
	data_lines := strings.Split(strings.Trim(string(data), "\n"), "\n")

	computer := NewComputer()
	instructions := []Instruction{}

	re_line := regexp.MustCompile(`(\w+) (\w+) ([-\d]+) if (\w+) ([!><=]+) ([-\d]+)`)

	for _, line := range data_lines {
		matches := re_line.FindStringSubmatch(line)

		register1 := matches[1]
		operation := matches[2]
		number1, _ := strconv.Atoi(matches[3])
		register2 := matches[4]
		comparison := matches[5]
		number2, _ := strconv.Atoi(matches[6])

		computer.add_register(register1)
		computer.add_register(register2)

		instructions = append(instructions, Instruction{register1, operation, number1, register2, comparison, number2})
	}
	return computer, instructions
}

func run_instructions(computer Computer, instructions []Instruction) {
	for _, i := range instructions {
		if computer.compare(i.register2, i.comparison, i.number2) {
			computer.operation(i.register1, i.operation, i.number1)
		}
	}
}

func solution(filename string) int {
	computer, instructions := parse(filename)
	run_instructions(computer, instructions)
	return computer.get_max_register()
}

func main() {
	fmt.Println(solution("./example.txt")) // 1
	fmt.Println(solution("./input.txt"))   // 3880
}
