package main

import (
	"fmt"
	"testing"
)

func TestGarbage(t *testing.T) {
	testCases := []struct {
		garbage  string
		expected int
	}{
		{"<>", 1},
		{"<random characters>", 18},
		{"<<<<>", 4},
		{"<{!>}>", 5},
		{"<!!>", 3},
		{"<!!!>>", 5},
		{"<{o\"i!a,<{i<a>", 13},
	}
	for _, tc := range testCases {
		t.Run(fmt.Sprintf("%s_should_be_%d", tc.garbage, tc.expected), func(t *testing.T) {
			result, _ := garbage(tc.garbage, 0)
			if result != tc.expected {
				t.Errorf("got %d; want %d", result, tc.expected)
			}
		})
	}
}

func TestPart1(t *testing.T) {
	testCases := []struct {
		data     string
		expected int
	}{
		{"{}", 1},
		{"{{{}}}", 6},
		{"{{},{}}", 5},
		{"{{{},{},{{}}}}", 16},
		{"{<a>,<a>,<a>,<a>}", 1},
		{"{{<ab>},{<ab>},{<ab>},{<ab>}}", 9},
		{"{{<!!>},{<!!>},{<!!>},{<!!>}}", 9},
		{"{{<a!>},{<a!>},{<a!>},{<ab>}}", 3},
	}
	for _, tc := range testCases {
		t.Run(fmt.Sprintf("%s_should_be_%d", tc.data, tc.expected), func(t *testing.T) {
			result, _ := parse_stream(tc.data)
			if result != tc.expected {
				t.Errorf("got %d; want %d", result, tc.expected)
			}
		})
	}
}

func TestPart2(t *testing.T) {
	testCases := []struct {
		data     string
		expected int
	}{
		{"<>", 0},
		{"<random characters>", 17},
		{"<<<<>", 3},
		{"<{!>}>", 2},
		{"<!!>", 0},
		{"<!!!>>", 0},
		{"<{o\"i!a,<{i<a>", 10},
	}
	for _, tc := range testCases {
		t.Run(fmt.Sprintf("%s_should_be_%d", tc.data, tc.expected), func(t *testing.T) {
			_, result := parse_stream(tc.data)
			if result != tc.expected {
				t.Errorf("got %d; want %d", result, tc.expected)
			}
		})
	}
}
