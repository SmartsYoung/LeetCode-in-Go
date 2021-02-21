package problem0103

import (
	"fmt"
	"testing"

	"github.com/SmartsYoung/LeetCode-in-Go/kit"

	"github.com/stretchr/testify/assert"
)

func Test_Problem0103(t *testing.T) {
	ast := assert.New(t)

	// tcs is testcase slice
	tcs := []struct {
		pre, in []int
		ans     [][]int
	}{

		{
			[]int{3, 9, 20, 15, 7},
			[]int{9, 3, 15, 20, 7},
			[][]int{
				[]int{3},
				[]int{20, 9},
				[]int{15, 7},
			},
		},

		// 可以多个 testcase
	}

	for _, tc := range tcs {
		fmt.Printf("~~%v~~\n", tc)

		ast.Equal(tc.ans, zigzagLevelOrder(kit.PreIn2Tree(tc.pre, tc.in)), "输入:%v", tc)
	}
}
