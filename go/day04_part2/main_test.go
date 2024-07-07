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
		{"abcde fghij", true},
		{"abcde xyz ecdab", false},
		{"a ab abc abd abf abj", true},
		{"iiii oiii ooii oooi oooo", true},
		{"oiii ioii iioi iiio", false},
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
