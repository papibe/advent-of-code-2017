package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
	"sync"
	"time"
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

	return program, registers
}

func run(
	program_id int,
	read_channel chan int,
	write_channel chan int,
	program []Instruction,
	registers map[string]int,
) int {
	var value int
	pointer := 0
	send_times := 0
	registers["p"] = program_id

	for {
		instr := program[pointer]

		switch instr.instruction {
		case SND:
			if is_alpha(instr.register) {
				value = registers[instr.register]
			} else {
				value, _ = strconv.Atoi(instr.register)
			}
			send_times++
			// if program_id == 1 {
			// 	fmt.Println(send_times)
			// }
			write_channel <- value

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
			select {
			case value = <-read_channel:
				registers[instr.register] = value
			case <-time.After(10 * time.Millisecond):
				// close(read_channel)
				// close(write_channel)
				fmt.Println("timeout", program_id, send_times)
				return 0
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
	return 0
}

func solution(filename string) int {
	program, registers := parse(filename)

	// copy registers
	registers2 := make(map[string]int)
	for k, v := range registers {
		registers2[k] = v
	}

	channel_a := make(chan int, 100)
	channel_b := make(chan int, 100)

	var wg sync.WaitGroup

	wg.Add(1)
	go run(0, channel_a, channel_b, program, registers)
	wg.Add(1)
	go run(1, channel_b, channel_a, program, registers2)

	wg.Wait()
	close(channel_a)
	close(channel_b)
	return 0
}

func main() {
	// fmt.Println(solution("./example2.txt")) // 3
	fmt.Println(solution("./input.txt")) // 7366
}
