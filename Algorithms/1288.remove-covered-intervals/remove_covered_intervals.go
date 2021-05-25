package main

import (
	"fmt"
	"sort"
)

type IntSlice [][]int

func (p IntSlice) Len() int { return len(p) }
func (p IntSlice) Less(i, j int) bool {
	if p[i][0] == p[j][0] {
		return p[i][1] < p[j][1]
	}
	return p[i][0] < p[j][0]
}
func (p IntSlice) Swap(i, j int) { p[i], p[j] = p[j], p[i] }

func removeCoveredIntervals(intervals [][]int) int {
	inter := IntSlice(intervals)
	sort.Sort(inter)

	for i := 0; i < len(inter)-1; {
		if inter[i][0] == inter[i+1][0] {
			inter = append(inter[:i], inter[i+1:]...)
			continue
		}
		if inter[i][1] >= inter[i+1][1] {
			inter = append(inter[:i+1], inter[i+2:]...)
			continue
		}
		i++
	}
	return len(inter)
}

func main() {
	interval := [][]int{{1, 4}, {3, 6}, {2, 8}}

	res := removeCoveredIntervals(interval)
	fmt.Println(res)
}
