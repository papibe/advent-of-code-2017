package main

import (
	"fmt"
	"testing"
)

func TestPart1(t *testing.T) {
	testCases := []struct {
		a_value  int
		b_value  int
		pairs    int
		expected int
	}{
		{65, 8921, 5, 1},
		{65, 8921, NUM_PAIRS, 588},
	}
	for _, tc := range testCases {
		t.Run(fmt.Sprintf("a starts %d, b starts %d, %d pairs, should be %d", tc.a_value, tc.b_value, tc.pairs, tc.expected), func(t *testing.T) {
			result := solution(tc.a_value, tc.b_value, tc.pairs)
			if result != tc.expected {
				t.Errorf("got %d; want %d", result, tc.expected)
			}
		})
	}
}
