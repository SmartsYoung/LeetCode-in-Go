# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # 迭代
        if not head:
            return None
        # 找到反转段
        cur, prev = head, None
        while m > 1:
            prev = cur
            cur = cur.next
            m, n = m-1, n-1
        tail, con = cur, prev
        # 三指针反转next指向
        while n:
            third = cur.next
            cur.next = prev
            prev = cur
            cur = third
            n -= 1
        # 将反转段链表整体翻转
        if con:
            con.next = prev
        else:
            head = prev
        tail.next = cur
        return head