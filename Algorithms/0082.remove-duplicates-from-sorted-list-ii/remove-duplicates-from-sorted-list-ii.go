package problem0082

import "fmt"

// ListNode is singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func deleteDuplicates(head *ListNode) *ListNode {
	dummy := &ListNode{}
	dummy.Next = head

	pre := dummy

	a := 200
	for pre.Next != nil {
		fmt.Println("num 1")
		if pre.Next.Val == a && pre.Next.Next == nil {
			fmt.Println("num 2")
			pre.Next = nil
			break
		}
		if pre.Next.Next != nil {
			fmt.Println("num 3")
			if pre.Next.Val == pre.Next.Next.Val {
				fmt.Println(pre.Next.Val)
				a = pre.Next.Val
				pre.Next = pre.Next.Next.Next
			} else if pre.Next.Val == a {
				a = pre.Next.Val
				pre.Next = pre.Next.Next
			} else {
				fmt.Println("num 4")
				pre = pre.Next
			}
		} else {
			break
		}
	}
	return dummy.Next
}

func deleteDuplicates1(head *ListNode) *ListNode {
	// 长度 <=1 的 list ，可以直接返回
	if head == nil || head.Next == nil {
		return head
	}

	// 要么 head 重复了，那就删除 head
	if head.Val == head.Next.Val {
		for head.Next != nil && head.Val == head.Next.Val {
			head = head.Next
		}
		return deleteDuplicates(head.Next)
	}

	// 要么 head 不重复，递归处理 head 后面的节点
	head.Next = deleteDuplicates(head.Next)
	return head
}
