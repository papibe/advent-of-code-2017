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
		{"example.txt", 100, 26},
		{"example.txt", 10_000_000, 2511944},
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
