package main

import (
	"fmt"
	"os"
	"regexp"
	"strings"
)

const ALL = -1

func parse(filename string) map[string][]string {
	data, err := os.ReadFile(filename)

	if err != nil {
		panic("file error")
	}
	data_lines := strings.Split(strings.Trim(string(data), "\n"), "\n")

	programs := make(map[string][]string)
	re_line := regexp.MustCompile(`^(\w+) \((\d+)\)`)

	for _, line := range data_lines {
		match := re_line.FindStringSubmatch(line)
		program := match[1]

		if strings.Contains(line, "->") {
			upper_programs := strings.Split(strings.Split(line, " -> ")[1], ", ")
			programs[program] = upper_programs

		} else {
			programs[program] = []string{}
		}
	}
	return programs
}

func solution(filename string) string {
	programs := parse(filename)
	program_with_parents := make(map[string]bool)

	for _, upper_programs := range programs {
		for _, uprogram := range upper_programs {
			program_with_parents[uprogram] = true
		}
	}

	for uprogram, _ := range program_with_parents {
		delete(programs, uprogram)
	}

	if len(programs) != 1 {
		panic("more than one root?")
	}

	for program, _ := range programs {
		return program
	}
	return ""
}

func main() {
	fmt.Println(solution("./example.txt")) // 5
	fmt.Println(solution("./input.txt"))   // 14029
}
