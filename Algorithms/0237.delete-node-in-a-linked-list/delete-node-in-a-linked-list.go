package problem0237

import "github.com/SmartsYoung/LeetCode-in-Go/kit"

// ListNode is pre-defined...
type ListNode = kit.ListNode

func deleteNode(node *ListNode) {
	node.Val = node.Next.Val
	node.Next = node.Next.Next
}
