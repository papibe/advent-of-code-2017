package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

type Position struct {
	x int
	y int
	z int
}

type Particle struct {
	x  int
	y  int
	z  int
	vx int
	vy int
	vz int
	ax int
	ay int
	az int
}

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

func parse(filename string) []Particle {
	data, err := os.ReadFile(filename)
	if err != nil {
		panic("Input file not found!")
	}
	lines := strings.Split((strings.Trim(string(data), "\n")), "\n")
	re := regexp.MustCompile(`p=<([-+]?\d+),([-+]?\d+),([-+]?\d+)>, v=<([-+]?\d+),([-+]?\d+),([-+]?\d+)>, a=<([-+]?\d+),([-+]?\d+),([-+]?\d+)>`)

	particles := []Particle{}

	for _, line := range lines {
		matches := re.FindStringSubmatch(line)

		// position
		x, _ := strconv.Atoi(matches[1])
		y, _ := strconv.Atoi(matches[2])
		z, _ := strconv.Atoi(matches[3])
		// velocity
		vx, _ := strconv.Atoi(matches[4])
		vy, _ := strconv.Atoi(matches[5])
		vz, _ := strconv.Atoi(matches[6])
		// acceleration
		ax, _ := strconv.Atoi(matches[7])
		ay, _ := strconv.Atoi(matches[8])
		az, _ := strconv.Atoi(matches[9])

		particles = append(particles, Particle{x, y, z, vx, vy, vz, ax, ay, az})
	}

	return particles
}

func solve(particles []Particle, cycles int) int {
	var current_positions map[Position][]Particle
	for range cycles {
		current_positions = make(map[Position][]Particle)

		for _, p := range particles {
			vx, vy, vz := p.vx+p.ax, p.vy+p.ay, p.vz+p.az
			x, y, z := p.x+vx, p.y+vy, p.z+vz

			position := Position{x, y, z}
			particle := Particle{x, y, z, vx, vy, vz, p.ax, p.ay, p.az}

			_, in_position := current_positions[position]
			if in_position {
				current_positions[position] = append(current_positions[position], particle)
			} else {
				current_positions[position] = []Particle{particle}
			}
		}

		particles = []Particle{}
		for _, parts := range current_positions {
			if len(parts) == 1 {
				particles = append(particles, parts[0])
			}
		}

	}

	return len(current_positions)
}

func solution(filename string) int {
	particles := parse(filename)
	return solve(particles, 1000)
}

func main() {
	fmt.Println(solution("./example.txt")) // 1
	fmt.Println(solution("./input.txt"))   // 707
}
