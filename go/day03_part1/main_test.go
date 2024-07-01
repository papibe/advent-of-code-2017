package main

import (
	"fmt"
	"testing"
)

func TestSolve(t *testing.T) {
	testCases := []struct {
		input    int
		expected int
	}{
		// initial
		{1, 0},
		// next square of size 3
		{2, 1},
		{3, 2},
		{4, 1},
		{5, 2},
		{6, 1},
		{7, 2},
		{8, 1},
		{9, 2},
		// next square of size 5
		{10, 3},
		{11, 2},
		{12, 3},
		{13, 4},
		{14, 3},
		{15, 2},
		{16, 3},
		{17, 4},
		{18, 3},
		{19, 2},
		{20, 3},
		{21, 4},
		{22, 3},
		{23, 2},
		{24, 3},
		{25, 4},
		{1024, 31},
	}
	for _, tc := range testCases {
		t.Run(fmt.Sprintf("%d_should_be_%d", tc.input, tc.expected), func(t *testing.T) {
			result := solution(tc.input)
			if result != tc.expected {
				t.Errorf("got %d; want %d", result, tc.expected)
			}
		})
	}
}
