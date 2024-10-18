package main

import (
	"fmt"
	"testing"
)

func TestPart1ExampleData(t *testing.T) {
	testCases := []struct {
		nodes_file string
		bursts     int
		expected   int
	}{
		{"example.txt", 7, 5},
		{"example.txt", 70, 41},
		{"example.txt", 10_000, 5587},
	}
	for _, tc := range testCases {
		t.Run(fmt.Sprintf("example with %d bursts should have infected %d", tc.bursts, tc.expected), func(t *testing.T) {
			result := solution(tc.nodes_file, tc.bursts)
			if result != tc.expected {
				t.Errorf("got %d; want %d", result, tc.expected)
			}
		})
	}
}
