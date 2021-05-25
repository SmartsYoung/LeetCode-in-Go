# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return None
        # 区间 [a, b) 包含 k 个待反转元素
        a, b = head, head
        for _ in range(k):
            if b is None:
                return head
            b = b.next
        # 反轉前K个元素
        newHead = self.reverse(a, b)
        # 递归反转后续链表并连接起来
        a.next = self.reverseKGroup(b, k)
        return newHead

    def reverse(self, a: ListNode, b: ListNode) -> ListNode:
        pre, cur, nxt = None, a, a
        while cur != b:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre
