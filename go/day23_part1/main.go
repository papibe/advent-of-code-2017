package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

const (
	SET = "set"
	MUL = "mul"
	SUB = "sub"
	JNZ = "jnz"
)

type Instruction struct {
	instruction string
	register    string
	param       string
}

func is_alpha(word string) bool {
	return regexp.MustCompile(`^[a-zA-Z]*$`).MatchString(word)
}

func parse(filename string) ([]Instruction, map[string]int) {
	data, err := os.ReadFile(filename)
	if err != nil {
		panic("Input file not found!")
	}

	lines := strings.Split((strings.Trim(string(data), "\n")), "\n")

	// parse program
	program := []Instruction{}
	for _, line := range lines {
		tokens := strings.Split(line, " ")

		param := ""
		if len(tokens) == 3 {
			param = tokens[2]
		}
		instruction := Instruction{tokens[0], tokens[1], param}
		program = append(program, instruction)
	}

	// create registers
	registers := make(map[string]int)
	for _, char := range "abcdefgh" {
		registers[string(char)] = 0
	}

	return program, registers
}

func run(program []Instruction, registers map[string]int) int {
	var value int
	pointer := 0
	mul_times := 0

	for pointer < len(program) {
		instr := program[pointer]

		switch instr.instruction {

		case SET:
			if is_alpha(instr.param) {
				value = registers[instr.param]
			} else {
				value, _ = strconv.Atoi(instr.param)
			}
			registers[instr.register] = value

		case SUB:
			if is_alpha(instr.param) {
				value = registers[instr.param]
			} else {
				value, _ = strconv.Atoi(instr.param)
			}
			registers[instr.register] -= value

		case MUL:
			mul_times++
			if is_alpha(instr.param) {
				value = registers[instr.param]
			} else {
				value, _ = strconv.Atoi(instr.param)
			}
			registers[instr.register] *= value

		case JNZ:
			var x int
			if is_alpha(instr.register) {
				x = registers[instr.register]
			} else {
				x, _ = strconv.Atoi(instr.register)
			}
			if is_alpha(instr.param) {
				value = registers[instr.param]
			} else {
				value, _ = strconv.Atoi(instr.param)
			}
			if x != 0 {
				pointer += value
				continue
			}

		default:
			fmt.Println(instr)
			panic("blah!")
		}
		pointer++

	}

	return mul_times
}

func solution(filename string) int {
	program, registers := parse(filename)
	return run(program, registers)
}

func main() {
	fmt.Println(solution("./input.txt")) // 6724
}
