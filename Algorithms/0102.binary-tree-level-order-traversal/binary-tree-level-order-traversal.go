package problem0102

import (
	"github.com/SmartsYoung/LeetCode-in-Go/kit"
)

type TreeNode = kit.TreeNode

func levelOrder(root *TreeNode) [][]int {
	res := [][]int{}

	if root == nil {
		return res
	}
	queue := make([]*TreeNode, 0)
	queue = append(queue, root)

	for len(queue) > 0 {
		length := len(queue)
		val := make([]int, 0)
		for i := 0; i < length; i++ {
			cur := queue[0]
			val = append(val, cur.Val)
			if cur.Left != nil {
				queue = append(queue, cur.Left)
			}
			if cur.Right != nil {
				queue = append(queue, cur.Right)
			}
			queue = queue[1:]
		}
		res = append(res, val)
	}

	return res
}
