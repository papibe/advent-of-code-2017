package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

const (
	SPIN int = iota
	EXCHANGE
	PARTNER
)

const BILLION = 1_000_000_000

type DanceMove struct {
	kind  int
	spin  int
	name1 int
	name2 int
	pos1  int
	pos2  int
}

type Dancer struct {
	name int
}

type Dancers struct {
	size int
	head int
	dict map[int]*Dancer
	list []*Dancer
}

func NewDancers(size int) Dancers {
	dict := make(map[int]*Dancer)
	list := []*Dancer{}

	for step := 0; step < size; step++ {
		name := 'a' + step
		dancer := &Dancer{name}
		list = append(list, dancer)
		dict[name] = dancer
	}
	head := 0

	return Dancers{size, head, dict, list}
}

func mod(a, b int) int {
	return (a%b + b) % b
}

func (d *Dancers) spin(number int) {
	d.head = mod(d.head-number, d.size)
}

func (d *Dancers) exchange(position1, position2 int) {
	// adjust positions
	pos1 := (d.head + position1) % d.size
	pos2 := (d.head + position2) % d.size

	// swap dancers
	d.list[pos1], d.list[pos2] = d.list[pos2], d.list[pos1]
}

func (d *Dancers) partner(name1, name2 int) {
	// swap values
	d.dict[name1].name, d.dict[name2].name = d.dict[name2].name, d.dict[name1].name

	// swap pointers
	d.dict[name1], d.dict[name2] = d.dict[name2], d.dict[name1]
}

func (d Dancers) get_dancers() string {
	output := []string{}
	for index := 0; index < d.size; index++ {
		name := d.list[mod(d.head+index, d.size)].name
		output = append(output, string(rune(name)))
	}
	return strings.Join(output, "")
}

func parse(filename string) []DanceMove {
	data, err := os.ReadFile(filename)

	if err != nil {
		panic("file error")
	}
	lines := strings.Trim(string(data), "\n")
	dance_moves := []DanceMove{}

	for _, move := range strings.Split(lines, ",") {
		var dance_move DanceMove

		switch move[0] {
		case 's':
			spin, _ := strconv.Atoi(move[1:])
			dance_move = DanceMove{SPIN, spin, 0, 0, 0, 0}
		case 'x':
			params := strings.Split(move[1:], "/")
			A, _ := strconv.Atoi(params[0])
			B, _ := strconv.Atoi(params[1])
			dance_move = DanceMove{EXCHANGE, 0, 0, 0, A, B}
		case 'p':
			params := strings.Split(move[1:], "/")
			A := int(params[0][0])
			B := int(params[1][0])
			dance_move = DanceMove{PARTNER, 0, A, B, 0, 0}
		default:
			panic("dirty file")
		}
		dance_moves = append(dance_moves, dance_move)
	}
	return dance_moves
}

func dance(dancers *Dancers, dance_moves []DanceMove) {
	for _, dance_move := range dance_moves {
		kind := dance_move.kind
		switch kind {
		case SPIN:
			dancers.spin(dance_move.spin)
		case EXCHANGE:
			dancers.exchange(dance_move.pos1, dance_move.pos2)
		case PARTNER:
			dancers.partner(dance_move.name1, dance_move.name2)
		default:
			panic("what?")
		}
	}
}

func solution(filename string, size int) string {
	dance_moves := parse(filename)
	dancers := NewDancers(size)

	seen := make(map[string]int)
	var index int
	var key string

	for index = 0; index < BILLION; index++ {
		key = dancers.get_dancers()
		_, has_seen := seen[key]
		if has_seen {
			break
		}
		seen[key] = index
		dance(&dancers, dance_moves)
	}
	prefix := seen[key]
	cycle := index - prefix
	reminding := (BILLION - prefix) % cycle

	for index = 0; index < reminding; index++ {
		dance(&dancers, dance_moves)
	}

	return dancers.get_dancers()
}

func main() {
	fmt.Println(solution("./input.txt", 16)) // "ifocbejpdnklamhg"
}
