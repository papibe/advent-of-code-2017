package main

import (
	"fmt"
	"testing"
)

var art2 = Art{
	{"#", ".", ".", "#"},
	{".", ".", ".", "."},
	{".", ".", ".", "."},
	{"#", ".", ".", "#"},
}

var art3 = Art{
	{"#", "#", ".", "#", "#", "."},
	{"#", ".", ".", "#", ".", "."},
	{".", ".", ".", ".", ".", "."},
	{"#", "#", ".", "#", "#", "."},
	{"#", ".", ".", "#", ".", "."},
	{".", ".", ".", ".", ".", "."},
}

func TestPart13Divisions(t *testing.T) {
	testCases := []struct {
		art      Art
		expected int
	}{
		{INITIAL_ART, 1},
	}
	for _, tc := range testCases {
		t.Run(fmt.Sprintf("INITIAL_ART first divisions should be %d", tc.expected), func(t *testing.T) {
			result := len(get_divisions(tc.art, 3))
			if result != tc.expected {
				t.Errorf("got %d; want %d", result, tc.expected)
			}
		})
	}
}

func TestPart12Divisions(t *testing.T) {
	testCases := []struct {
		art      Art
		expected int
	}{
		{art2, 4},
		{art3, 9},
	}
	for _, tc := range testCases {
		t.Run(fmt.Sprintf("art first divisions should be %d", tc.expected), func(t *testing.T) {
			result := len(get_divisions(tc.art, 2))
			if result != tc.expected {
				t.Errorf("got %d; want %d", result, tc.expected)
			}
		})
	}
}
