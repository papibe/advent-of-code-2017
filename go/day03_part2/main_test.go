package main

import (
	"fmt"
	"testing"
)

func TestSolve(t *testing.T) {
	testCases := []struct {
		start    int
		end      int
		expected int
	}{
		{1, 1, 2},
		{2, 3, 4},
		{4, 4, 5},
		{5, 9, 10},
		{10, 10, 11},
		{11, 22, 23},
		{23, 24, 25},
		{25, 25, 26},
		{26, 53, 54},
		{54, 56, 57},
		{57, 58, 59},
		{59, 121, 122},
		{122, 132, 133},
		{133, 141, 142},
		{142, 146, 147},
		{147, 303, 304},
		{304, 329, 330},
		{330, 350, 351},
		{351, 361, 362},
		{362, 746, 747},
	}
	for _, tc := range testCases {
		t.Run(fmt.Sprintf("from_%d_to_%d_should_%d", tc.start, tc.end, tc.expected), func(t *testing.T) {
			for parameter := tc.start; parameter <= tc.end; parameter++ {
				result := solution(parameter)
				if result != tc.expected {
					t.Errorf("got %d; want %d", result, tc.expected)
				}
			}
		})
	}
}
