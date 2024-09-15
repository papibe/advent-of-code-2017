package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

const (
	SND = "snd"
	SET = "set"
	ADD = "add"
	MUL = "mul"
	MOD = "mod"
	RCV = "rcv"
	JGZ = "jgz"
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
	for _, ins := range program {
		if is_alpha(ins.register) {
			registers[ins.register] = 0
		}
		if is_alpha(ins.param) {
			registers[ins.param] = 0
		}
	}

	// add sound register
	registers["snd"] = 0

	return program, registers

}

func run(program []Instruction, registers map[string]int) int {
	pointer := 0
	var value int

exit:
	for {
		instr := program[pointer]

		switch instr.instruction {
		case SND:
			registers[SND] = registers[instr.register]

		case SET:
			if is_alpha(instr.param) {
				value = registers[instr.param]
			} else {
				value, _ = strconv.Atoi(instr.param)
			}
			registers[instr.register] = value

		case ADD:
			if is_alpha(instr.param) {
				value = registers[instr.param]
			} else {
				value, _ = strconv.Atoi(instr.param)
			}
			registers[instr.register] += value

		case MUL:
			if is_alpha(instr.param) {
				value = registers[instr.param]
			} else {
				value, _ = strconv.Atoi(instr.param)
			}
			registers[instr.register] *= value

		case MOD:
			if is_alpha(instr.param) {
				value = registers[instr.param]
			} else {
				value, _ = strconv.Atoi(instr.param)
			}
			registers[instr.register] %= value

		case RCV:
			if is_alpha(instr.register) {
				value = registers[instr.register]
			} else {
				value, _ = strconv.Atoi(instr.register)
			}
			if value != 0 {
				break exit
			}

		case JGZ:
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
			if x > 0 {
				pointer += value
				continue
			}
		}
		pointer++

	}

	return registers["snd"]
}

func solution(filename string) int {
	program, registers := parse(filename)
	return run(program, registers)
}

func main() {
	fmt.Println(solution("./example1.txt")) // 4
	fmt.Println(solution("./input.txt"))    // 2951
}
