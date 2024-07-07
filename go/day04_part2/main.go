package main

import (
	"fmt"
	"os"
	"sort"
	"strings"
)

func parse(filename string) []string {
	data, err := os.ReadFile(filename)

	if err != nil {
		panic("file error")
	}
	return strings.Split(strings.Trim(string(data), "\n"), "\n")
}

func sort_string(word string) string {
	s := strings.Split(word, "")
	sort.Strings(s)
	return strings.Join(s, "")
}

func is_valid(line string) bool {
	words := strings.Split(line, " ")

	unique_words := make(map[string]bool)
	for _, word := range words {
		unique_words[sort_string(word)] = true
	}

	return len(words) == len(unique_words)
}

func solution(filename string) int {
	data := parse(filename)

	valid_passphrases := 0
	for _, line := range data {
		if is_valid(line) {
			valid_passphrases += 1
		}
	}
	return valid_passphrases
}

func main() {
	fmt.Println(solution("./input.txt")) // 251
}
