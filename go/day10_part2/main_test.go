package main

import (
	"fmt"
	"testing"
)

func TestPart1(t *testing.T) {
	testCases := []struct {
		input    string
		size     int
		expected string
	}{

		{"", 256, "a2582a3a0e66e6e86e3812dcb672a272"},
		{"AoC 2017", 256, "33efeb34ea91902bb2f59c9920caa6cd"},
		{"1,2,3", 256, "3efbe78a8d82f29979031a4aa0b16a9d"},
		{"1,2,4", 256, "63960835bcdc130f0b66d7ff4f6a5a8e"},
	}
	for _, tc := range testCases {
		t.Run(fmt.Sprintf("'%s'_should_be_%s", tc.input, tc.expected), func(t *testing.T) {
			result := solve(tc.input, tc.size)
			if result != tc.expected {
				t.Errorf("got %s; want %s", result, tc.expected)
			}
		})
	}
}
