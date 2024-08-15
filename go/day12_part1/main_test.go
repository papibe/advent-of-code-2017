package main

import (
	"fmt"
	"testing"
)

func TestPart1(t *testing.T) {
	testCases := []struct {
		directions []string
		expected   int
	}{
		{[]string{"ne", "ne", "ne"}, 3},
		{[]string{"ne", "ne", "sw", "sw"}, 0},
		{[]string{"ne", "ne", "s", "s"}, 2},
		{[]string{"se", "sw", "se", "sw", "sw"}, 3},
	}
	for _, tc := range testCases {
		t.Run(fmt.Sprintf("%s_should_be_%d", tc.directions, tc.expected), func(t *testing.T) {
			result := solve(tc.directions)
			if result != tc.expected {
				t.Errorf("got %d; want %d", result, tc.expected)
			}
		})
	}
}
