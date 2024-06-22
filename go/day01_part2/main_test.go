package main

import (
	"fmt"
	"testing"
)

func TestSolve(t *testing.T) {
	testCases := []struct {
		input    string
		expected int
	}{
		{"1212", 6},
		{"1221", 0},
		{"123425", 4},
		{"123123", 12},
		{"12131415", 4},
	}
	for _, tc := range testCases {
		t.Run(fmt.Sprintf("%s->%d", tc.input, tc.expected), func(t *testing.T) {
			result := solve(tc.input)
			if result != tc.expected {
				t.Errorf("got %d; want %d", result, tc.expected)
			}
		})
	}
}
