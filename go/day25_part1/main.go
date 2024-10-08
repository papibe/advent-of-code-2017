package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

type Rule struct {
	write      int
	movement   int
	next_state string
}

type State struct {
	name  string
	rules map[int]Rule
}

func (c *State) add_rule(value, write int, movement string, next_state string) {
	var move int
	if movement == "right" {
		move = 1
	} else {
		move = -1
	}
	c.rules[value] = Rule{write, move, next_state}
}

func (c State) get_write_value(value int) int {
	return c.rules[value].write
}

func (c State) get_movement(value int) int {
	return c.rules[value].movement
}

func (c State) get_next_state(value int) string {
	return c.rules[value].next_state
}

type Tape struct {
	tape map[int]bool
}

func (t Tape) get_value(position int) int {
	_, ok := t.tape[position]
	if ok {
		return 1
	}
	return 0
}

func (t *Tape) set_value(position int, value int) {
	_, position_in_tape := t.tape[position]

	if value == 0 && position_in_tape {
		delete((*t).tape, position)
		return
	}
	if value == 0 && !position_in_tape {
		return
	}

	(*t).tape[position] = true
}

func (t Tape) len() int {
	return len(t.tape)
}

func parse(filename string) (string, int, map[string]State) {
	data, err := os.ReadFile(filename)
	if err != nil {
		panic("Input file not found!")
	}

	blocks := strings.Split((strings.Trim(string(data), "\n")), "\n\n")

	// parse header
	header_str := `Begin in state (\w).
Perform a diagnostic checksum after (\d+) steps.`

	header_re := regexp.MustCompile(header_str)
	match := header_re.FindStringSubmatch(blocks[0])

	initial_state := match[1]
	steps, _ := strconv.Atoi(match[2])

	// parse states
	block_re := regexp.MustCompile(`In state (\w):
  If the current value is (\d):
    - Write the value (\d).
    - Move one slot to the (\w+).
    - Continue with state (\w).
  If the current value is (\d):
    - Write the value (\d).
    - Move one slot to the (\w+).
    - Continue with state (\w).`)

	states := make(map[string]State)

	for _, block := range blocks[1:] {
		match := block_re.FindStringSubmatch(block)

		state_name := match[1]
		state := State{state_name, make(map[int]Rule)}

		// first rule
		current_value, _ := strconv.Atoi(match[2])
		write_value, _ := strconv.Atoi(match[3])
		movement := match[4]
		next_state := match[5]
		state.add_rule(current_value, write_value, movement, next_state)

		// second rule
		current_value, _ = strconv.Atoi(match[6])
		write_value, _ = strconv.Atoi(match[7])
		movement = match[8]
		next_state = match[9]
		state.add_rule(current_value, write_value, movement, next_state)

		states[state_name] = state
	}
	return initial_state, steps, states
}

func solve(initial_state string, steps int, states map[string]State, tape Tape) int {
	current_position := 0
	current_state := initial_state

	for range steps {
		state := states[current_state]

		current_value := tape.get_value(current_position)
		write_value := state.get_write_value(current_value)
		tape.set_value(current_position, write_value)

		current_position += state.get_movement(current_value)
		current_state = state.get_next_state(current_value)
	}
	return tape.len()
}

func solution(filename string) int {
	initial_state, steps, states := parse(filename)
	tape := Tape{make(map[int]bool)}
	return solve(initial_state, steps, states, tape)
}

func main() {
	fmt.Println(solution("./example.txt")) // 3
	fmt.Println(solution("./input.txt"))   // 633
}
