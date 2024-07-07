package main

import (
	"fmt"
	"testing"
)

func TestSolve(t *testing.T) {
	testCases := []struct {
		passphrases string
		expected    bool
	}{
		{"aa bb cc dd ee", true},
		{"aa bb cc dd aa", false},
		{"aa bb cc dd aaa", true},
	}
	for _, tc := range testCases {
		t.Run(fmt.Sprintf("%s_should_be_%t", tc.passphrases, tc.expected), func(t *testing.T) {
			result := is_valid(tc.passphrases)
			if result != tc.expected {
				t.Errorf("got %t; want %t", result, tc.expected)
			}
		})
	}
}
