package main

import (
	"fmt"
	"math"
	"os"
	"regexp"
	"strconv"
	"strings"
)

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

func solve(particles []Particle, cycles, tolerance int) int {
	repetitions := 0
	min_particle := 0
	previous_min_particle := 0

	for range cycles {
		new_particles := []Particle{}
		for _, p := range particles {
			vx, vy, vz := p.vx+p.ax, p.vy+p.ay, p.vz+p.az
			x, y, z := p.x+vx, p.y+vy, p.z+vz
			new_particles = append(new_particles, Particle{x, y, z, vx, vy, vz, p.ax, p.ay, p.az})
		}

		particles = new_particles

		// look for min distance in this cycle
		min_distance := math.MaxInt
		for index, p := range new_particles {
			distance := abs(p.x) + abs(p.y) + abs(p.z)
			if distance < min_distance {
				min_particle = index
				min_distance = distance
			}
		}
		if min_particle == previous_min_particle {
			repetitions++
		} else {
			repetitions = 0
		}

		if repetitions >= tolerance {
			return min_particle
		}
	}

	return min_particle
}

func solution(filename string) int {
	particles := parse(filename)
	return solve(particles, 1000, 300)
}

func main() {
	fmt.Println(solution("./example.txt")) // 0
	fmt.Println(solution("./input.txt"))   //258
}
