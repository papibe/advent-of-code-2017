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
		{"1122", 3},
		{"1111", 4},
		{"1234", 0},
		{"91212129", 9},
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
