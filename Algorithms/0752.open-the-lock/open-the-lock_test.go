package problem0752

import (
	"fmt"
	"testing"

	"github.com/stretchr/testify/assert"
)

// tcs is testcase slice
var tcs = []struct {
	deadends []string
	target   string
	ans      int
}{
	{
		[]string{"0201", "0101", "0102", "1212", "2002"},
		"0202",
		6,
	},

	{
		[]string{"8888"},
		"0000",
		0,
	},

	{
		[]string{"8888"},
		"0009",
		1,
	},

	{
		[]string{"8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"},
		"8888",
		-1,
	},

	{
		[]string{"0000"},
		"8888",
		-1,
	},
	{
		deadends: []string{"5557", "5553", "5575", "5535", "5755", "5355", "7555", "3555", "6655", "6455", "4655", "4455", "5665", "5445", "5645", "5465", "5566", "5544", "5564", "5546", "6565", "4545", "6545", "4565", "5656", "5454", "5654", "5456", "6556", "4554", "4556", "6554"},
		target:   "5555",
		ans:      -1,
	},

	// 可以有多个 testcase
}

func Test_fn(t *testing.T) {
	ast := assert.New(t)

	for _, tc := range tcs {
		fmt.Printf("~~%v~~\n", tc)
		ast.Equal(tc.ans, openLock(tc.deadends, tc.target), "输入:%v", tc)
	}
}

func Benchmark_fn(b *testing.B) {
	for i := 0; i < b.N; i++ {
		for _, tc := range tcs {
			openLock(tc.deadends, tc.target)
		}
	}
}
